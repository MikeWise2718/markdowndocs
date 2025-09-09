---
title: "ComfyUI"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
github - (https://github.com/comfyanonymous/ComfyUI)

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
## Windows
- You can install multiple versions of python on windows by default
- If you need an old version
   - Go get an AMD64 installer msi of the right version
   - an old version (the last one in the series that has an installer and not just a security update)
   - For example python 3.10.11 is here: (https://www.python.org/downloads/release/python-31011/)
   = For example python 3.12.10 is here: (https://www.python.org/downloads/release/python-31210/
   - Make sure you click "Add Python to path" at installation time
- `py --list` will list what versions you have available
- `py -3.12 -m venv .venv` to install it
- `.venv\Scripts\activate`

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
   - Windows CUDA Archive - Old Versions: (https://developer.nvidia.com/cuda-toolkit-archive)
   - `pip install torch torchvision torchaudio  --index-url https://download.pytorch.org/whl/cu118`
   - `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
   - `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128`
   - As of June 2025, the official pre-built PyTorch wheels only support up to CUDA 12.8.
   - Test with `python; import torch; torch.cuda.is_available()`
- Install other dependencies:
   - `pip install -r requirements.txt`
- Download models:
   - Place the necessary Stable Diffusion models (e.g., checkpoints) in the `ComfyUI/models/checkpoints` directory.
- Launch ComfyUI:
   -  `python3 main.py`


# Installing Node Manager
- `cd <your ComfyUI install>/ComfyUI/custom_nodes`
- `git clone https://github.com/ltdrdata/ComfyUI-Manager.git`

# Models
- Reside on Hugging face or civitai
- Best way to find them is to ask Perplexity as HF search often doesn't workcd

## CIVITAI
- https://civitai.com/
- mikewise1618471

## Tensor.Art
- https://tensor.art/
- 