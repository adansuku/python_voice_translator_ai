import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

# Load configuration from .env file
config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

# Constants
MODEL_NAME = "base"
ELEVENLABS_VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam
ELEVENLABS_MODEL_ID = "eleven_turbo_v2"
OUTPUT_FORMAT = "mp3_22050_32"
VOICE_SETTINGS = VoiceSettings(
    stability=0.0,
    similarity_boost=0.0,
    style=0.0,
    use_speaker_boost=True,
)

def load_whisper_model():
    """Load the Whisper model."""
    return whisper.load_model(MODEL_NAME)

def transcribe_audio(model, audio_file):
    """Transcribe audio using the Whisper model."""
    try:
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
        return transcription
    except Exception as e:
        raise gr.Error(f"An error occurred while transcribing the text: {str(e)}")

def translate_text(transcription):
    """Translate the transcription to multiple languages."""
    translations = {}
    try:
        translations['en'] = Translator(from_lang="es", to_lang="en").translate(transcription)
        translations['it'] = Translator(from_lang="es", to_lang="it").translate(transcription)
        translations['fr'] = Translator(from_lang="es", to_lang="fr").translate(transcription)
        translations['ja'] = Translator(from_lang="es", to_lang="ja").translate(transcription)
        return translations
    except Exception as e:
        raise gr.Error(f"An error occurred while translating the text: {str(e)}")

def text_to_speech(client, text, language):
    """Convert text to speech using ElevenLabs API."""
    try:
        response = client.text_to_speech.convert(
            voice_id=ELEVENLABS_VOICE_ID,
            optimize_streaming_latency="0",
            output_format=OUTPUT_FORMAT,
            text=text,
            model_id=ELEVENLABS_MODEL_ID,
            voice_settings=VOICE_SETTINGS,
        )
        
        save_file_path = f"{language}.mp3"
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
        return save_file_path
    except Exception as e:
        raise gr.Error(f"An error occurred while creating the audio: {str(e)}")

def handle_translation(audio_file):
    """Handle the overall translation process."""
    model = load_whisper_model()
    transcription = transcribe_audio(model, audio_file)
    print(f"Original text: {transcription}")
    
    translations = translate_text(transcription)
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    audio_files = {lang: text_to_speech(client, text, lang) for lang, text in translations.items()}
    return tuple(audio_files.values())

# Gradio Interface
web = gr.Interface(
    fn=handle_translation,
    inputs=gr.Audio(sources=["microphone"], type="filepath", label="Spanish"),
    outputs=[
        gr.Audio(label="English"),
        gr.Audio(label="Italian"),
        gr.Audio(label="French"),
        gr.Audio(label="Japanese")
    ],
    title="Voice Translator",
    description="AI-powered voice translator to multiple languages"
)

web.launch()
