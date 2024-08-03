
# Voice Translator

## Overview

Voice Translator is an AI-powered application that transcribes audio from Spanish to text and translates it into multiple languages. It then converts the translated texts into audio files. This project uses Gradio for the user interface, Whisper for audio transcription, and ElevenLabs for text-to-speech conversion.

## Features

-   Transcribe Spanish audio to text.
-   Translate the transcribed text into English, Italian, French, and Japanese.
-   Convert the translated texts into audio files.
-   Display the original transcription along with the translated audios.

## Installation

### Prerequisites

-   Python 3.7 or higher
    
-   `ffmpeg` installed on your system. You can install it via Homebrew on macOS:
    
    `brew install ffmpeg`
    

### Clone the repository

`git clone https://github.com/your-username/voice-translator.git`

`cd voice-translator`

### Create the virtual environment

`python3 -m venv .venv`

`source .venv/bin/activate` # On Windows use `.venv\Scripts\activate`

### Install the requirements

`pip install -r requirements.txt`

### Create a `.env` file in the root directory and add your ElevenLabs API key:

`ELEVENLABS_API_KEY=your_elevenlabs_api_key`

## Usage

### Activate the virtual environment if it's not already activated:

`source .venv/bin/activate` # On Windows use `.venv\Scripts\activate`

### Run the application:

`python main.py`

### Open the provided URL in your browser to access the Gradio interface.

Use the microphone input to provide Spanish audio. The application will transcribe the audio, translate it into multiple languages, and generate audio files for each translation.

## Project Structure

voice-translator/ 
│ 
├── .venv/ # Virtual environment 
├── .env # Environment variables 
├── main.py # Main application file 
├── requirements.txt # Required Python packages 
└── README.md # This README file

## Dependencies and Acknowledgements

-   `gradio`: For creating the web interface.
-   `openai-whisper`: For audio transcription.
-   `translate`: For text translation.
-   `python-dotenv`: For loading environment variables.
-   `elevenlabs`: For text-to-speech conversion.