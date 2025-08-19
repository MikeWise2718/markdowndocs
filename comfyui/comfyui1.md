---
title: "ComfiUI"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
github - (https://github.com/comfyanonymous/ComfyUI_

# Installation

- you will need the right python venv - currently 3.12
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
sudo apt install python3.12-dev
sudo apt install python3.12-venv
python3.12 --version
```
- For windows there are no deadsnakes, so you can maybe use chocolatey (choco) to install python3.12

## Then do the following
- Clone the repository:
  - `git clone https://github.com/comfyanonymous/ComfyUI.git`
- Navigate to the directory: `cd ComfyUI`
- Create a virtual environment:
  -  `python3.12 -m venv venv`
- Activate the environment:
  - `source venv/bin/activate` on Linux or MacOS
  - `venv\Scripts\activate` on Windows
- Install dependencies:
   - Install PyTorch with CUDA or ROCm support according to your GPU. The exact commands vary, so consult the official ComfyUI installation instructions or relevant guides for your system.
   - `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
   - `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
   - As of June 2025, the official pre-built PyTorch wheels only support up to CUDA 12.8.
   - Test with python; import torch; torch.cuda.is_available()
- Install other dependencies:
   - `pip install -r requirements.txt`
- Download models:
   - Place the necessary Stable Diffusion models (e.g., checkpoints) in the `ComfyUI/models/checkpoints` directory.
- Launch ComfyUI:
   -  `python3 main.py`


## CIVITAI
- https://civitai.com/
- mikewise1618471