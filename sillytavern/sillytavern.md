---
title: "SillyTavern"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# SillyTavern
SillyTavern (or ST for short) is a locally installed user interface that allows you to interact with text generation LLMs, image generation engines, and TTS voice models.

- Repo -  https://github.com/SillyTavern/SillyTavern
- Docs - https://docs.sillytavern.app/ 
- Installation and first steps YT by NerdyRodent:  https://www.youtube.com/watch?v=bHqJ6mo1P-4 
- Need to download and install ollama and run a model, ollama should then be in the path

## Character Card Libraries
- There are two versions of the json data
   - V1 - https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v1.md
   - V2 - https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md 
- https://aicharactercards.com/
   - V1 cards
- https://character-tavern.com/ 
   - V1 cards
- https://chub.ai/search 
   - V2 cards
- Character Editor: https://zoltanai.github.io/character-editor/
  - Note if flags an json format error, click on the details, the json is often to be seen there if it is not V2
- Program (seems to only do V2)
- to find text in notepad++, open file (it is binary so it will look wierd), then search for "tEXtchara", then copy the text after the null until the == into a base64 decoder
   - https://www.base64decode.org/ 
  

# Olama
- download web site: https://ollama.com/download/windows
- Hugging face Dolphin Mixtral 8x7b -  https://huggingface.co/TheBloke/dolphin-2.7-mixtral-8x7b-GGUF
- `ollama run hf.co/mradermacher/dolphin-2.7-mixtral-8x7b-GGUF:Q4_K_M`
  - will download that model from hf, put it in its models directory, and run it
- `ollama list` will show you what models you have installed

# Startup
- Its a bit complicated, need to start ollama, then ComfyUI, then SillyTavern
- Step-by-step:
    - Start ollama from a new cmd propmt: `ollama run llama3.2`
    - Start Comfyui from another new cmd prompt:
    - `d:`
    - `cd Comfyui`
    - `.venv\Scripts\activate`
    - `python main.py`
    - Start SillyTavern from a third new cmd prompt: 
    - `d:`
    - `cd \typescript\SillyTavern-Launcher`
    - `Launcher.bat`
    - Enter 1 to upgrade and start



