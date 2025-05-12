# STAR: Video Super-Resolution and Enhancement

STAR is a comprehensive video processing toolkit that combines multiple state-of-the-art models for video super-resolution and enhancement.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (RTX 4090 recommended)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/STAR.git
cd STAR
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# OR
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required models:
```bash
python download_models.py
```

### Running the Web Application

1. Start the backend server:
```bash
cd webapp/backend
pip install -r requirements.txt
python main.py
```

2. Start the frontend development server:
```bash
cd webapp/frontend
npm install
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

### Running from Command Line

1. Place your input video in `./input/video/`
2. Add your prompt to `./input/text/prompt.txt`
3. Run the inference script:
```bash
bash ./video_super_resolution/scripts/inference_sr.sh
```

## 📁 Project Structure

```
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
STAR/
├── video_super_resolution/    # Video super-resolution models
├── cogvideox-based/          # CogVideoX implementation
├── webapp/                   # Web application
│   ├── backend/             # FastAPI backend
│   └── frontend/            # React frontend
├── input/                   # Input files
│   ├── video/              # Input videos
│   └── text/               # Text prompts
├── output/                 # Output files
├── requirements.txt        # Python dependencies
└── download_models.py      # Model download script
```

## 🛠️ Available Models

- **I2VGen-XL**: Light and heavy degradation models
- **CogVideoX-5B**: Advanced video generation model

## 🌐 Web Interface Features

- Video upload with drag-and-drop
- Video preview
- Model selection
- Real-time processing status
- Result video display and download
- Processing history (coming soon)
- Batch processing (coming soon)
- Custom model configurations (coming soon)

## 🐛 Known Issues

- WebSocket connection may need reconnection logic for long-running processes
- Large file uploads need proper handling
- Temporary files need proper cleanup
- CUDA out-of-memory errors need graceful handling
- Failed processing jobs need proper error handling

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
*Last Updated: 2024-02-20*

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
![STAR