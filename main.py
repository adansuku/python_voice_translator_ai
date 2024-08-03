import gradio as gr
import whisper as wh
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings


dotenv_values(".env")

ELEVEN_API_KEY = dotenv_values(".env")["ELEVEN_API_KEY"]

def tanslator(audio_file):
    try:
        model = wh.load_model("base")
        result = model.transcribe(audio_file, fp16=False)
        transcription = result['text']
    except Exception as e:
        raise gr.Error(
            f"Error something went wrong creating the audio file: {e}"
        )
    
    print(f"transcription: {transcription}")
    
    try:
        en_transciption = Translator(to_lang="en").translate(transcription)
    except Exception as e:
        raise gr.Error(
            f"Error, something failed on translation: {e}"
        )
        
    print(f"translation: {en_transciption}")
        
    try:
        client = ElevenLabs(api_key=ELEVEN_API_KEY)
        print(ELEVEN_API_KEY)
        
        response = client.text_to_speech.convert(
                voice_id="Xb7hH8MSUJpSbSDYk0k2",  # A sweet girl :)
                optimize_streaming_latency="0",
                output_format="mp3_22050_32",
                text=en_transciption,
                model_id="eleven_turbo_v2",  
                voice_settings=VoiceSettings(
                    stability=0.0,
                    similarity_boost=1.0,
                    style=0.0,
                    use_speaker_boost=True,
                )
            )

        save_file_path = "audios/en.mp3"
        with open(save_file_path, "wb") as file:
            for chunk in response:
                if chunk:
                    file.write(chunk)
    except Exception as e:
        raise gr.Error(
            f"Error, something failed when the audio was created: {e}"
        )
        
    return save_file_path

web = gr.Interface(
    fn=tanslator, 
    inputs=gr.Audio(
        sources=["microphone"], 
        type="filepath"
        ), 
    outputs=[gr.Audio(label="Translated Audio")],
    title= "Audio Transcription",
    description= "Transcribe audio from your microphone"
    )

web.launch(share=True)