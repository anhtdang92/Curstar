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

def run_i2vgenxl_super_resolution_test():
    """Run I2VGen-XL based super-resolution inference test with progress tracking."""
    logger.info("Starting I2VGen-XL Super-Resolution inference test...")
    
    # Import here to ensure proper environment setup
    try:
        from video_super_resolution.scripts.inference_sr import main as inference_main
        logger.info("Successfully imported inference module")
    except ImportError as e:
        logger.error(f"Failed to import inference module: {e}")
        return False

    # Set up arguments as Namespace object
    # Using light_deg.pt as an example for I2VGen-XL based super-resolution
    # Ensure this model path and input video path are correct for your setup
    args = Namespace(
        solver_mode='fast',
        steps=15,
        input_path='input/video/023_klingai_reedit.mp4', # Using the original test video
        model_path='./pretrained_models/I2VGen-XL-based/light_deg.pt', # I2VGen-XL model
        prompt='A high-resolution, clear video of a person walking in a city street', # Prompt suitable for this video
        upscale=4,
        max_chunk_len=32, # Reset to a more moderate value for this video
        file_name='023_klingai_reedit_i2vgenxl_sr.mp4', # Output file name for this video
        save_dir='./results/i2vgenxl_test',
        show_progress=True  # Enable progress bar
    )
    
    # Create save directory if it doesn't exist
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
        logger.info(f"Created save directory: {args.save_dir}")

    try:
        logger.info("Starting I2VGen-XL inference process...")
        start_time = time.time()
        
        # Run inference
        inference_main(args)
        
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"I2VGen-XL inference completed successfully in {duration:.2f} seconds")
        
        # Check if output file exists
        output_path = os.path.join(args.save_dir, args.file_name)
        if os.path.exists(output_path):
            logger.info(f"Output video saved to: {output_path}")
            return True
        else:
            logger.error(f"Output video not found at {output_path}")
            return False
            
    except Exception as e:
        logger.error(f"Error during I2VGen-XL inference: {e}")
        return False

if __name__ == "__main__":
    print("Running I2VGen-XL Super-Resolution inference test...")
    success = run_i2vgenxl_super_resolution_test()
    if success:
        print("\nTest completed successfully!")
    else:
        print("\nTest failed. Check the logs above for details.") 