import os
import sys
import logging
from tqdm import tqdm
import time
from argparse import Namespace

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def run_star_inference():
    """Run STAR inference with progress tracking."""
    logger.info("Starting STAR inference test...")
    
    # Import here to ensure proper environment setup
    try:
        from video_super_resolution.scripts.inference_sr import main as inference_main
        logger.info("Successfully imported inference module")
    except ImportError as e:
        logger.error(f"Failed to import inference module: {e}")
        return False

    # Set up arguments as Namespace object
    args = Namespace(
        solver_mode='fast',
        steps=15,
        input_path='input/video/023_klingai_reedit.mp4',
        model_path='./pretrained_models/cogvideox/transformer/CogVideoX-5B-based/1/mp_rank_00_model_states.pt',
        prompt='A person walking in a city street with buildings in the background',
        upscale=4,
        max_chunk_len=32,
        file_name='023_klingai_reedit.mp4',
        save_dir='./results/cogvideox_test',
        show_progress=True  # Enable progress bar
    )

    try:
        logger.info("Starting inference process...")
        start_time = time.time()
        
        # Run inference
        inference_main(args)
        
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Inference completed successfully in {duration:.2f} seconds")
        
        # Check if output file exists
        output_path = os.path.join('./results/cogvideox_test', '023_klingai_reedit.mp4')
        if os.path.exists(output_path):
            logger.info(f"Output video saved to: {output_path}")
            return True
        else:
            logger.error("Output video not found")
            return False
            
    except Exception as e:
        logger.error(f"Error during inference: {e}")
        return False

if __name__ == "__main__":
    print("Running STAR inference test...")
    success = run_star_inference()
    if success:
        print("\nTest completed successfully!")
    else:
        print("\nTest failed. Check the logs above for details.") 