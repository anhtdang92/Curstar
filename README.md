<div align="center">
    <h1>
    STAR: Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution
    </h1>
    <div>
        <a href='https://github.com/CSRuiXie' target='_blank'>Rui Xie<sup>1*</sup></a>,&emsp;
        <a href='https://github.com/yhliu04' target='_blank'>Yinhong Liu<sup>1*</sup></a>,&emsp;
        <a href='https://scholar.google.com/citations?hl=zh-CN&user=yWq1Fd4AAAAJ' target='_blank'>Penghao Zhou<sup>2</sup></a>,&emsp;
        <a href='https://scholar.google.com/citations?user=Uhp3JKgAAAAJ&hl=zh-CN&oi=sra' target='_blank'>Chen Zhao<sup>1</sup></a>,&emsp;
        <a href='https://scholar.google.com/citations?hl=zh-CN&user=w03CHFwAAAAJ' target='_blank'>Jun Zhou<sup>3</sup></a><br>
        <a href='https://cszn.github.io/' target='_blank'>Kai Zhang<sup>1</sup></a>,&emsp;
        <a href='https://jessezhang92.github.io/' target='_blank'>Zhenyu Zhang<sup>1</sup></a>,&emsp;
        <a href='https://scholar.google.com.hk/citations?user=6CIDtZQAAAAJ&hl=zh-CN' target='_blank'>Jian Yang<sup>1</sup></a>,&emsp;
        <a href='https://scholar.google.com/citations?hl=zh-CN&user=Ds5wwRoAAAAJ' target='_blank'>Zhenheng Yang<sup>2</sup></a>,&emsp;
        <a href='https://tyshiwo.github.io/index.html' target='_blank'>Ying Tai<sup>1&#8224</sup></a>
    </div>
    <div>
        <sup>1</sup>Nanjing University,&emsp;<sup>2</sup>ByteDance,&emsp; <sup>3</sup>Southwest University
    </div>
    <div>
        <h4 align="center">
            <a href="https://nju-pcalab.github.io/projects/STAR" target='_blank'>
                <img src="https://img.shields.io/badge/🌟-Project%20Page-blue" style="padding-right: 20px;">
            </a>
            <a href="https://arxiv.org/abs/2501.02976" target='_blank'>
                <img src="https://img.shields.io/badge/arXiv-2501.02976-b31b1b.svg" style="padding-right: 20px;">
            </a>
            <a href="https://youtu.be/hx0zrql-SrU" target='_blank'>
                <img src="https://img.shields.io/badge/Demo%20Video-%23FF0000.svg?logo=YouTube&logoColor=white" style="padding-right: 20px;">
            </a>
            <br>
            <a href="https://huggingface.co/spaces/SherryX/STAR" target='_blank'>
                <img src="https://img.shields.io/static/v1?label=Demo STAR&message=HuggingFace&color=yellow">
            </a>
            <a href="https://colab.research.google.com/drive/1K8A1U_BNpAteRhhW9A8pAYs6LWjItQs_?usp=sharing" target='_blank'>
                <img src="https://img.shields.io/static/v1?label=Demo STAR&message=Google Colab&color=orange">
            </a>
        </h4>
    </div>
</div>


## 🔆 Updates
- **2025.01.19** The STAR demo is now available on [Google Colab](https://colab.research.google.com/drive/1K8A1U_BNpAteRhhW9A8pAYs6LWjItQs_?usp=sharing). Feel free to give it a try!

- **2025.01.09** The online demo of STAR on [Hugging Face](https://huggingface.co/spaces/SherryX/STAR) is now live! Please note that due to the duration limitation of ZeroGPU, the running time may exceed the allocated GPU duration. If you'd like to try it, you can duplicate the demo and assign a paid GPU.

- **2025.01.07**  The pretrained STAR model (I2VGen-XL and CogVideoX-5B versions) and inference code have been released.


## 📑 TODO
- [ ] Training codes
- [x] Inference codes
- [x] Online demo


## 🔎 Method Overview
![STAR](assets/overview.png)


## 📷 Results Display
![STAR](assets/teaser.png)
![STAR](assets/real_world.png)
👀 More visual results can be found in our [Project Page](https://nju-pcalab.github.io/projects/STAR) and [Video Demo](https://youtu.be/hx0zrql-SrU).


## ⚙️ Dependencies and Installation
**VRAM requirement**: Upscaling the provided toy example by 4x, with 72 frames, a width of 426, and a height of 240, requires around 39GB of VRAM using the default settings. If you encounter an OOM problem, you can set a smaller frame_length in inference_sr.sh. We recommend using a GPU with at least 24GB of VRAM to run this project. 

**Python Environment**: This project requires Python 3.10. 

**NumPy Version**: This project requires NumPy < 2.0. It has been tested with NumPy 1.26.4. Please ensure you have a compatible version installed.

```
## git clone this repository
git clone https://github.com/anhtdang92/Curstar.git
cd Curstar

## create an environment (choose one)
# Using conda:
conda create -n star python=3.10
conda activate star
# Using venv:
python -m venv venv
# Activate venv (Windows):
.\venv\Scripts\Activate.ps1
# Activate venv (Linux/Mac):
source venv/bin/activate

pip install -r requirements.txt
```

### Model Files Checklist
To run STAR, you must have the following model files in place:

- `pretrained_models/cogvideox/vae/3d-vae.pt`
- `pretrained_models/cogvideox/transformer/CogVideoX-5B-based/1/mp_rank_00_model_states.pt`
- `pretrained_models/cogvideox/t5-v1_1-xxl/` directory containing:
    - model-00001-of-00002.safetensors
    - model-00002-of-00002.safetensors
    - model.safetensors.index.json
    - config.json
    - tokenizer_config.json
    - special_tokens_map.json
    - added_tokens.json
    - spiece.model

If any of these files are missing, use the provided `download_models.py` script to fetch them automatically, or download them manually from the official Hugging Face links in the script.

**Note:** After successful model setup, you may see folders like `temp_t5`, `temp_cogvideox`, or `temp_cogvideo` in your project directory. These are temporary folders created during model downloads and are not needed for running STAR. You can safely delete them to keep your workspace clean.

### Troubleshooting Model Downloads
- If you encounter issues with model downloads, check your internet connection and available disk space.
- For manual download, see: https://huggingface.co/THUDM/CogVideoX-2b

---

## 🚀 Inference

### Model Weight
| Base Model | Type | URL |
|------------|--------|-----------------------------------------------------------------------------------------------|
| I2VGen-XL | Light Degradation | [:link:](https://huggingface.co/SherryX/STAR/resolve/main/I2VGen-XL-based/light_deg.pt?download=true) |
| I2VGen-XL | Heavy Degradation | [:link:](https://huggingface.co/SherryX/STAR/resolve/main/I2VGen-XL-based/heavy_deg.pt?download=true) |
| CogVideoX-5B | Heavy Degradation | [:link:](https://huggingface.co/SherryX/STAR/tree/main/CogVideoX-5B-based) |

### 1. I2VGen-XL-based 
#### Step 1: Download the pretrained model STAR from [HuggingFace](https://huggingface.co/SherryX/STAR).
We provide two versions for I2VGen-XL-based model, `heavy_deg.pt` for heavy degraded videos and `light_deg.pt` for light degraded videos (e.g., the low-resolution video downloaded from video websites).

You can put the weight into `pretrained_weight/`.

#### Step 2: Prepare testing data
You can put the testing videos in the `input/video/`.

As for the prompt, there are three options: 1. No prompt. 2. Automatically generate a prompt (e.g., [using Pllava](https://github.com/hpcaitech/Open-Sora/tree/main/tools/caption#pllava-captioning)). 3. Manually write the prompt. You can put the txt file in the `input/text/`.


#### Step 3: Change the path
You need to change the paths in `video_super_resolution/scripts/inference_sr.sh` to your local corresponding paths, including `video_folder_path`, `txt_file_path`, `model_path`, and `save_dir`.


#### Step 4: Running inference command
```
bash video_super_resolution/scripts/inference_sr.sh
```

**Note on `inference_sr.sh`**: This shell script is a convenient way to process multiple videos located in `input/video/` using prompts from `input/text/prompt.txt`. It iterates through video-prompt pairs and calls the underlying `video_super_resolution/scripts/inference_sr.py` script. Ensure the paths within the shell script (`video_folder_path`, `txt_file_path`, `model_path`, `save_dir`) are correctly set. The python script `inference_sr.py` has also been updated to correctly use `ArgumentParser` (resolving a previous `NameError`). This shell script is now confirmed to work in a `bash` environment (e.g., Git Bash on Windows) by directly calling the virtual environment's Python executable.

### 2. CogVideoX-based
Refer to these [instructions](https://github.com/NJU-PCALab/STAR/tree/main/cogvideox-based#cogvideox-based-model-inference) for inference with the CogVideX-5B-based model.

Please note that the CogVideX-5B-based model supports only 720x480 input.

## Automated Inference Test

You can test your STAR installation and model setup with the provided script:

```bash
python test_star_inference.py
```

This will run a sample inference using the test video and model, with a progress bar enabled. The output will be saved to `./results/cogvideox_test/023_klingai_reedit.mp4`.

If you encounter errors, check the output for troubleshooting information.

## ❤️ Acknowledgments
This project is based on [I2VGen-XL](https://github.com/ali-vilab/VGen), [VEnhancer](https://github.com/Vchitect/VEnhancer), [CogVideoX](https://github.com/THUDM/CogVideo) and [OpenVid-1M](https://github.com/NJU-PCALab/OpenVid-1M). Thanks for their awesome works.


## 🎓Citations
If our project helps your research or work, please consider citing our paper:

```
@misc{xie2025starspatialtemporalaugmentationtexttovideo,
      title={STAR: Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution}, 
      author={Rui Xie and Yinhong Liu and Penghao Zhou and Chen Zhao and Jun Zhou and Kai Zhang and Zhenyu Zhang and Jian Yang and Zhenheng Yang and Ying Tai},
      year={2025},
      eprint={2501.02976},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2501.02976}, 
}
```


## 📧 Contact
If you have any inquiries, please don't hesitate to reach out via email at `ruixie0097@gmail.com`


## 📄 License
I2VGen-XL-based models are distributed under the terms of the [MIT License](https://choosealicense.com/licenses/mit/).

CogVideoX-5B-based model is distributed under the terms of the [CogVideoX License](https://huggingface.co/THUDM/CogVideoX-5b/blob/main/LICENSE).

## Cursor Instructions
For detailed instructions on setting up and using this project, please refer to the `.cursor.yaml` file in the root directory. This file contains step-by-step guidelines for installation, usage, and additional notes.

## Running Tests
We provide a convenient PowerShell script to run the STAR inference tests with the correct environment setup:

```powershell
.\run_test.ps1
```

This script handles:
- Virtual environment activation
- PYTHONPATH configuration
- Running the inference test

The script ensures that all necessary environment variables are set correctly, making it easier to run tests consistently.

## Model Files Checklist
Before running inference, ensure you have the following model files in place:

### For I2VGen-XL-based model:
- `pretrained_models/i2vgenxl/transformer/i2vgenxl_5b_infer_sr.yaml`
- `pretrained_models/i2vgenxl/transformer/i2vgenxl_5b_infer_sr/1/mp_rank_00_model_states.pt`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/config.json`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/model.safetensors.index.json`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/model-00001-of-00002.safetensors`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/model-00002-of-00002.safetensors`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/spiece.model`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/special_tokens_map.json`
- `pretrained_models/i2vgenxl/t5-v1_1-xxl/added_tokens.json`

### For CogVideoX-based model:
- `pretrained_models/cogvideox/transformer/CogVideoX-5B-based/1/mp_rank_00_model_states.pt`
- `pretrained_models/cogvideox/t5-v1_1-xxl/config.json`
- `pretrained_models/cogvideox/t5-v1_1-xxl/model.safetensors.index.json`
- `pretrained_models/cogvideox/t5-v1_1-xxl/model-00001-of-00002.safetensors`
- `pretrained_models/cogvideox/t5-v1_1-xxl/model-00002-of-00002.safetensors`
- `pretrained_models/cogvideox/t5-v1_1-xxl/spiece.model`
- `pretrained_models/cogvideox/t5-v1_1-xxl/special_tokens_map.json`
- `pretrained_models/cogvideox/t5-v1_1-xxl/added_tokens.json`

## Running Inference

### I2VGen-XL-based Model
1. Change the paths in `i2vgenxl-based/sat/configs/i2vgenxl_5b/i2vgenxl_5b_infer_sr.yaml` to match your local paths.
2. Run inference:
   ```bash
   python i2vgenxl-based/sat/sample_sr.py
   ```

### CogVideoX-based Model
1. Change the paths in `cogvideox-based/sat/configs/cogvideox_5b/cogvideox_5b_infer_sr.yaml` to match your local paths.
2. Run inference:
   ```bash
   python cogvideox-based/sat/sample_sr.py
   ```

## Troubleshooting
If you encounter any issues with model downloads, try:
1. Checking your internet connection
2. Verifying the model file paths
3. Ensuring all required files are present
4. Checking file permissions
