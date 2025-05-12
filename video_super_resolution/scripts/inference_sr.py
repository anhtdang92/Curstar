import os
import torch
from argparse import ArgumentParser, Namespace
import json
from typing import Any, Dict, List, Mapping, Tuple
from easydict import EasyDict

import sys
import logging
from tqdm import tqdm
import time

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_path)
from video_to_video.video_to_video_model import VideoToVideo_sr
from video_to_video.utils.seed import setup_seed
from video_to_video.utils.logger import get_logger
from video_super_resolution.color_fix import adain_color_fix

from inference_utils import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class STAR():
    def __init__(self, 
                 result_dir='./results/',
                 file_name='000_video.mp4',
                 model_path='',
                 solver_mode='fast',
                 steps=15,
                 guide_scale=7.5,
                 upscale=4,
                 max_chunk_len=32,
                 show_progress=False,
                 ):
        self.model_path=model_path
        logger.info('checkpoint_path: {}'.format(self.model_path))

        self.result_dir = result_dir
        self.file_name = file_name
        os.makedirs(self.result_dir, exist_ok=True)

        model_cfg = EasyDict(__name__='model_cfg')
        model_cfg.model_path = self.model_path
        model_cfg.show_progress = show_progress
        self.model = VideoToVideo_sr(model_cfg)

        steps = 15 if solver_mode == 'fast' else steps
        self.solver_mode=solver_mode
        self.steps=steps
        self.guide_scale=guide_scale
        self.upscale = upscale
        self.max_chunk_len=max_chunk_len
        self.show_progress = show_progress

    def enhance_a_video(self, video_path, prompt):
        logger.info('input video path: {}'.format(video_path))
        text = prompt
        logger.info('text: {}'.format(text))
        caption = text + self.model.positive_prompt

        input_frames, input_fps = load_video(video_path)
        logger.info('input fps: {}'.format(input_fps))

        video_data = preprocess(input_frames)
        _, _, h, w = video_data.shape
        logger.info('input resolution: {}'.format((h, w)))
        target_h, target_w = h * self.upscale, w * self.upscale   # adjust_resolution(h, w, up_scale=4)
        logger.info('target resolution: {}'.format((target_h, target_w)))

        pre_data = {'video_data': video_data, 'y': caption}
        pre_data['target_res'] = (target_h, target_w)

        total_noise_levels = 900
        setup_seed(666)

        with torch.no_grad():
            data_tensor = collate_fn(pre_data, 'cuda:0')
            output = self.model.test(data_tensor, total_noise_levels, steps=self.steps, \
                                solver_mode=self.solver_mode, guide_scale=self.guide_scale, \
                                max_chunk_len=self.max_chunk_len,
                                show_progress=self.show_progress
                                )

        output = tensor2vid(output)

        # Using color fix
        output = adain_color_fix(output, video_data)

        save_video(output, self.result_dir, self.file_name, fps=input_fps)
        return os.path.join(self.result_dir, self.file_name)
    

def parse_args():
    parser = argparse.ArgumentParser(description='STAR Video Super-Resolution')
    parser.add_argument('--solver_mode', type=str, default='fast', help='Solver mode')
    parser.add_argument('--steps', type=int, default=15, help='Number of steps')
    parser.add_argument('--input_path', type=str, required=True, help='Input video path')
    parser.add_argument('--model_path', type=str, required=True, help='Model path')
    parser.add_argument('--prompt', type=str, required=True, help='Text prompt')
    parser.add_argument('--upscale', type=int, default=4, help='Upscale factor')
    parser.add_argument('--max_chunk_len', type=int, default=32, help='Maximum chunk length')
    parser.add_argument('--file_name', type=str, required=True, help='Output file name')
    parser.add_argument('--save_dir', type=str, required=True, help='Save directory')
    parser.add_argument('--show_progress', action='store_true', help='Show progress bar')
    return parser.parse_args()

def main(args):
    """Main function for STAR inference with progress tracking."""
    logger.info("Initializing STAR inference...")
    start_time = time.time()

    try:
        # Initialize STAR model
        logger.info("Loading model...")
        star = STAR(
            result_dir=args.save_dir,
            file_name=args.file_name,
            model_path=args.model_path,
            solver_mode=args.solver_mode,
            steps=args.steps,
            upscale=args.upscale,
            max_chunk_len=args.max_chunk_len,
            show_progress=args.show_progress
        )
        
        # Process video
        logger.info("Processing video...")
        output_path = star.enhance_a_video(args.input_path, args.prompt)
        
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Processing completed in {duration:.2f} seconds")
        logger.info(f"Output saved to: {output_path}")
        
    except Exception as e:
        logger.error(f"Error during inference: {e}")
        raise

if __name__ == "__main__":
    args = parse_args()
    main(args)
