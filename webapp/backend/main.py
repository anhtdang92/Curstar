import logging
# Configure basic logging FIRST to capture all subsequent logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import platform

# Set asyncio policy for Windows
if platform.system() == "Windows":
    logger.info("Attempting to set WindowsSelectorEventLoopPolicy...")
    try:
        # Try setting the policy first (more standard)
        # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        # If the above doesn't work reliably, try forcing the loop directly:
        selector_loop = asyncio.SelectorEventLoop()
        asyncio.set_event_loop(selector_loop)
        logger.info("Successfully set asyncio event loop to SelectorEventLoop directly.")
    except Exception as e:
        logger.error(f"Failed to set asyncio event loop policy/loop: {e}")

# Log the current event loop type after attempting to set the policy
current_loop = asyncio.get_event_loop()
logger.info(f"Current asyncio event loop: {type(current_loop).__name__}")

# --- Core Imports ---
from fastapi import FastAPI, UploadFile, File, WebSocket, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel # Ensure BaseModel is imported here
from typing import List, Dict, Any
import os
import shutil
import uuid
from datetime import datetime # Keep datetime import if needed elsewhere
import json
# --- End Core Imports ---

app = FastAPI(title="STAR Video Processing API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create necessary directories
UPLOAD_DIR = "uploads"
RESULTS_DIR = "results"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Available models
AVAILABLE_MODELS = [
    {
        "id": "i2vgenxl_light",
        "name": "I2VGen-XL (Light Degradation)",
        "description": "Best for videos with minor quality issues"
    },
    {
        "id": "i2vgenxl_heavy",
        "name": "I2VGen-XL (Heavy Degradation)",
        "description": "Best for videos with severe quality issues"
    },
    {
        "id": "cogvideox",
        "name": "CogVideoX-5B",
        "description": "Advanced model for high-quality video enhancement"
    }
]

class ProcessRequest(BaseModel):
    filename: str
    model: str

# --- Job Status Tracking ---
# Dictionary to store the status and progress of processing jobs
# Key: job_id (filename), Value: Dict with progress info
job_statuses: Dict[str, Dict[str, Any]] = {}
# Lock for thread-safe access to job_statuses (though FastAPI runs endpoints in async normally)
# Using a simple dict might be sufficient for asyncio, but a Lock is safer if threading involved later
job_status_lock = asyncio.Lock()
# --- End Job Status Tracking ---

@app.get("/")
async def read_root():
    return {"message": "STAR Video Processing API"}

@app.get("/models")
async def get_models():
    return AVAILABLE_MODELS

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    # Generate unique filename
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename": unique_filename,
        "original_name": file.filename,
        "size": os.path.getsize(file_path)
    }

async def run_inference_process(filename: str, model: str):
    """Runs the inference script as a subprocess and updates job status."""
    job_id = filename
    python_executable = "../venv/Scripts/python.exe" # Adjust if necessary
    script_path = "../video_super_resolution/scripts/inference_sr.py"
    input_path = os.path.abspath(os.path.join(UPLOAD_DIR, filename))
    output_dir = os.path.abspath(RESULTS_DIR)
    output_filename = filename # Use the same unique name for output
    model_path_map = { # Map model IDs to actual model file paths
        "i2vgenxl_light": "../../pretrained_models/I2VGen-XL-based/light_deg.pt", # Corrected path
        "i2vgenxl_heavy": "../../pretrained_models/I2VGen-XL-based/heavy_deg.pt", # Corrected path
        "cogvideox": "../../pretrained_models/cogvideox/transformer/CogVideoX-5B-based/1/mp_rank_00_model_states.pt" # Corrected path relative to backend
    }
    model_file_path = os.path.abspath(model_path_map.get(model, ""))

    # TODO: Get actual prompt - for now, use a placeholder
    prompt = "Enhance this video"

    if not os.path.exists(model_file_path):
        error_msg = f"Model file not found for {model}: {model_file_path}"
        logger.error(error_msg)
        async with job_status_lock:
            job_statuses[job_id] = {'status': 'failed', 'error': error_msg, 'progress': 0}
        return

    command = [
        python_executable,
        script_path,
        '--input_path', input_path,
        '--model_path', model_file_path,
        '--prompt', prompt,
        '--file_name', output_filename,
        '--save_dir', output_dir,
        # Add other necessary args like --steps, --solver_mode, etc. if needed
        # '--show_progress' # Optional: Keep tqdm locally if desired
    ]

    logger.info(f"Running command: {' '.join(command)}")

    # Update initial status
    async with job_status_lock:
        job_statuses[job_id] = {'status': 'processing', 'progress': 0}

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=".." # Run from the parent directory (STAR/)
    )

    # Process stdout stream for progress updates
    if process.stdout:
        while True:
            line_bytes = await process.stdout.readline()
            if not line_bytes:
                break
            line = line_bytes.decode().strip()
            if line.startswith('{') and line.endswith('}'): # Check if it looks like our JSON progress
                try:
                    progress_data = json.loads(line)
                    async with job_status_lock:
                        # Merge new data with existing status, ensuring status remains 'processing'
                        current_status = job_statuses.get(job_id, {})
                        current_status.update(progress_data)
                        current_status['status'] = 'processing' # Keep status as processing
                        job_statuses[job_id] = current_status
                    logger.debug(f"Job {job_id} progress: {progress_data}")
                except json.JSONDecodeError:
                    logger.warning(f"Non-JSON output from subprocess: {line}")
            else:
                 # Log other stdout lines if needed (might be logs from script)
                 logger.info(f"Subprocess ({job_id}) stdout: {line}")

    # Wait for process completion and handle errors
    stdout, stderr = await process.communicate()

    async with job_status_lock:
        if process.returncode == 0:
             # Ensure final progress is 100% on success
            final_status = job_statuses.get(job_id, {})
            final_status.update({'status': 'complete', 'progress': 100})
            job_statuses[job_id] = final_status
            logger.info(f"Job {job_id} completed successfully.")
        else:
            error_output = stderr.decode().strip()
            job_statuses[job_id] = {'status': 'failed', 'error': error_output, 'progress': job_statuses.get(job_id, {}).get('progress', 0)}
            logger.error(f"Job {job_id} failed. Return code: {process.returncode}")
            logger.error(f"Stderr: {error_output}")

@app.post("/process")
async def process_video(request: ProcessRequest, background_tasks: BackgroundTasks):
    filename = request.filename
    model = request.model
    valid_model_ids = [m["id"] for m in AVAILABLE_MODELS]
    if model not in valid_model_ids:
        raise HTTPException(status_code=400, detail="Invalid model selection")

    input_file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(input_file_path):
        raise HTTPException(status_code=404, detail="Uploaded file not found")

    job_id = filename # Use filename as job ID

    # Check if job already running
    async with job_status_lock:
        if job_id in job_statuses and job_statuses[job_id]['status'] == 'processing':
            raise HTTPException(status_code=409, detail="Processing already in progress for this file")
        # Initialize status before starting background task
        job_statuses[job_id] = {'status': 'queued', 'progress': 0}

    # Run the inference process in the background
    background_tasks.add_task(run_inference_process, filename, model)

    return {
        "status": "queued",
        "message": f"Processing job queued for {filename} with {model}",
        "job_id": job_id
    }

# WebSocket endpoint for progress updates
@app.websocket("/ws/{job_id}")
async def websocket_endpoint(websocket: WebSocket, job_id: str):
    await websocket.accept()
    logger.info(f"WebSocket connection established for job_id: {job_id}")

    last_sent_status = None
    try:
        while True:
            async with job_status_lock:
                current_status = job_statuses.get(job_id)

            if current_status:
                # Only send if status has changed since last send
                if current_status != last_sent_status:
                    await websocket.send_json(current_status)
                    last_sent_status = current_status.copy() # Store a copy
                    logger.debug(f"Sent status for job {job_id}: {current_status}")

                # Stop sending if job is complete or failed
                if current_status.get('status') in ['complete', 'failed']:
                    logger.info(f"Job {job_id} finished with status: {current_status.get('status')}. Closing WebSocket.")
                    break
            else:
                # Job ID not found (yet?), wait briefly
                # Could send a 'waiting' status initially
                pass 

            await asyncio.sleep(1) # Check for updates every second

    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for job_id: {job_id}")
    except Exception as e:
        logger.error(f"WebSocket error for job_id {job_id}: {e}")
    finally:
        # Ensure connection is closed gracefully
        try:
            await websocket.close()
        except RuntimeError as e:
             # Ignore errors if connection already closed
             if "WebSocket is not connected" not in str(e):
                  logger.warning(f"Error closing WebSocket for {job_id}: {e}")
        logger.info(f"WebSocket connection closed for job_id: {job_id}")

# Modify get_result to use job_id (filename)
@app.get("/results/{job_id}")
async def get_result(job_id: str):
    file_path = os.path.join(RESULTS_DIR, job_id)
    # Check job status first
    async with job_status_lock:
        status = job_statuses.get(job_id)
    
    if not status or status.get('status') != 'complete':
         raise HTTPException(status_code=404, detail="Result not ready or job failed")

    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        # This case might indicate an issue if status is complete but file doesn't exist
        logger.error(f"Result file expected but not found for completed job {job_id} at {file_path}")
        raise HTTPException(status_code=404, detail="Result file not found despite completed status")

if __name__ == "__main__":
    import uvicorn
    # Logging is configured above
    logger.info("Starting FastAPI server...")
    # Explicitly tell uvicorn to use the standard asyncio loop setup
    uvicorn.run("main:app", host="0.0.0.0", port=8000, loop="asyncio") 