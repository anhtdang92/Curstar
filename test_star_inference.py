import os
import subprocess

# Parameters for STAR inference
test_cmd = [
    'python',
    'video_super_resolution/scripts/inference_sr.py',
    '--solver_mode', 'fast',
    '--steps', '15',
    '--input_path', 'input/video/023_klingai_reedit.mp4',
    '--model_path', './pretrained_models/cogvideox/transformer/CogVideoX-5B-based/1/mp_rank_00_model_states.pt',
    '--prompt', 'A person walking in a city street with buildings in the background',
    '--upscale', '4',
    '--max_chunk_len', '32',
    '--file_name', '023_klingai_reedit.mp4',
    '--save_dir', './results/cogvideox_test',
    '--progress'
]

if __name__ == '__main__':
    print('Running STAR inference test...')
    result = subprocess.run(test_cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print('Errors:', result.stderr) 