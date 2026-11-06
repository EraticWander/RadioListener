# Radio Stream DeepSpeech Listener (`RadioListener`)

A lightweight Python client that continuously connects to a live AAC audio stream (e.g., `streamtheworld.com`), decodes audio chunks in memory using `pydub`, converts them to 16-bit mono PCM WAV buffers, and performs local offline speech-to-text transcription using **Mozilla DeepSpeech (`0.9.3`)**.

---

## Features

- **In-Memory Stream Decoding**:
  - Streams live AAC audio over HTTP (`requests`), converts chunks via `pydub.AudioSegment` and `numpy` without writing temporary audio files to disk.
- **Offline Speech-to-Text (`deepspeech`)**:
  - Uses local acoustic (`deepspeech-0.9.3-models.pbmm`) and language scorer (`deepspeech-0.9.3-models.scorer`) models for zero-cost continuous transcription.

---

## Prerequisites & Model Setup

Because the pre-trained DeepSpeech 0.9.3 model files exceed GitHub's 100 MB file limit (~180 MB and ~909 MB), they are excluded via `.gitignore`. Ensure the following two files are present in the project root before running:

- `deepspeech-0.9.3-models.pbmm`
- `deepspeech-0.9.3-models.scorer`

```bash
# Download DeepSpeech 0.9.3 models if not already present locally:
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```

Also ensure `ffmpeg` is installed on your system (required by `pydub` for AAC decoding):

```bash
sudo apt-get install ffmpeg
```

---

## Usage

```bash
python3 -m venv env
source env/bin/activate
pip install deepspeech pydub numpy requests
python main.py
```

---

## Credits, Acknowledgments & External Sources

- **[Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech)** *(MPL-2.0 License)*  
  Open-source embedded Speech-to-Text engine and pre-trained acoustic/KenLM scorer models (`v0.9.3`) developed by **Mozilla**, based on Baidu's *Deep Speech: Scaling up end-to-end speech recognition* research paper (Hannun et al.).
- **[`pydub`](https://github.com/jiaaro/pydub)** *(MIT License)* & **[FFmpeg](https://github.com/FFmpeg/FFmpeg)** *(LGPL-2.1 / GPL)*  
  Created by **James Robert (`jiaaro`)** (`pydub`) and the **FFmpeg Team**, used for decoding live AAC audio streams into PCM WAV samples in memory.
- **[NumPy](https://github.com/numpy/numpy)** & **[Requests](https://github.com/psf/requests)**  
  Used for audio buffer array manipulation and HTTP stream consumption.
