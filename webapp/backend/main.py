from fastapi import FastAPI, UploadFile, File, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import shutil
import uuid
from typing import List
import asyncio
from datetime import datetime
from pydantic import BaseModel

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

@app.post("/process")
async def process_video(request: ProcessRequest):
    filename = request.filename
    model = request.model
    valid_model_ids = [m["id"] for m in AVAILABLE_MODELS]
    if model not in valid_model_ids:
        return {"error": "Invalid model selection"}
    # TODO: Implement actual video processing using STAR
    # This is where we'll integrate the existing STAR processing code
    # For now, just return a mock response
    return {
        "status": "processing",
        "message": f"Processing {filename} with {model}",
        "timestamp": datetime.now().isoformat()
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # TODO: Implement real-time progress updates
            await websocket.send_json({"status": "processing", "progress": 0})
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

@app.get("/results/{filename}")
async def get_result(filename: str):
    file_path = os.path.join(RESULTS_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "Result file not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 