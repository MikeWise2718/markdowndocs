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


# Misc Repos
- ComfyUI -  `git clone https://github.com/comfyanonymous/ComfyUI.git`
- ComfyUI Node Manager - `git clone https://github.com/ltdrdata/ComfyUI-Manager.git`
- WD14 Reverse Tagger - `git clone https://github.com/pythongosssss/ComfyUI-WD14-Tagger`
- image2prompt - `git clone https://github.com/zhongpei/Comfyui_image2prompt` 

# Installing Node Manager
- `cd d:/ComfyUI/custom_nodes`
- `git clone https://github.com/ltdrdata/ComfyUI-Manager.git`

# Installing 

# Models
- Reside on Hugging face or civitai
- Best way to find them is to ask Perplexity as HF search often doesn't workcd

## CIVITAI
- https://civitai.com/
- mikewise1618471

## Tensor.Art
- https://tensor.art/


## uv Installation 
- got it out of a perplexity space
- uv notes - `https://codemaker2016.medium.com/introducing-uv-next-gen-python-package-manager-b78ad39c95d7`

### Step-by-step
- Clone Comfy UI into your directory - `git clone https://github.com/comfyanonymous/ComfyUI.git comfyui0`
- Change into rep directory = cd `confyui0` 
- Create venv - `uv venv`
- Install the appropriate versoin of Pytorch - `uv pip install torch torchvision torchaudio --torch-backend=cu128`
   - `.venv\Scripts\Activate`
   - `python -c "import torch; print(torch.cuda.is_available())"` 
   - If it is not `True`, you need to fix it.
- Install ComfyUI dependencies - `uv pip install -r requirements.txt`
   - Maybe this happens automagicaly when we installed torch? 
- Optionally uv lock it - `uv lock`
    - This creates a `uv.lock` file with all the dependencies in it
- Run it - `uv run python main.py` 

