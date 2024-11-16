# Audio Transcription Script

A simple Python script for transcribing audio files into text using OpenAI's Whisper API.

---

## Features
- Manage your OpenAI API key securely with a `config.ini` file.
- Convert audio files to text using the Whisper model.
- Save transcription to a default or custom output file.

---

## Requirements
- Python 3.7+
- OpenAI Python SDK (`pip install openai`)

---

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/audio-transcription.git
   cd audio-transcription
   ```

2. **Install denpendecies**
   In a python virtualenv :
   ```bash
   pip install openai
   ```

## Usage
1. Set Your API Key
   Save your OpenAI API key to the config.ini file:
    ```bash
    python transcribe_audio.py set_api_key <your_openai_api_key>
    ```

2. Transcribe Audio
Run the script to transcribe an audio file:
   ```bash
   python transcribe_audio.py <path_to_audio_file> [<output_file_path>]
   ```   
  - path_to_audio_file: Path to the audio file (required).
  - output_file_path: Path to save the transcription (optional).


## Example
   ```bash
   python transcribe_audio.py sample_audio.mp3
   ```
This saves the transcription as sample_audio.txt.

