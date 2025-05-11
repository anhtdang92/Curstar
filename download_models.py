import os
import shutil
import requests
from tqdm import tqdm

def download_file(url, local_path):
    """Download a file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    with open(local_path, 'wb') as f, tqdm(
        desc=os.path.basename(local_path),
        total=total_size,
        unit='iB',
        unit_scale=True
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            pbar.update(size)

def main():
    # Create T5 model directory
    t5_dir = "pretrained_models/cogvideox/t5-v1_1-xxl"
    os.makedirs(t5_dir, exist_ok=True)

    # T5 model files to download
    t5_files = [
        "model-00001-of-00002.safetensors",
        "model-00002-of-00002.safetensors",
        "model.safetensors.index.json",
        "config.json",
        "tokenizer_config.json",
        "special_tokens_map.json",
        "added_tokens.json",
        "spiece.model"
    ]

    print("Downloading T5 model files...")
    for file in t5_files:
        try:
            print(f"\nDownloading {file}...")
            url = f"https://huggingface.co/THUDM/CogVideoX-2b/resolve/main/{file}"
            local_path = os.path.join(t5_dir, file)
            download_file(url, local_path)
            print(f"Successfully downloaded {file}")
        except Exception as e:
            print(f"Error downloading {file}: {str(e)}")

    print("\nDone downloading T5 model files!")

if __name__ == "__main__":
    main() 