import gradio as gr
import whisper as wh
from tanslate import Translator

def tanslator(audio_file):
    try:
        model = wh.load_model("base")
        result = model.transcribe(audio_file)
        transciption = result['text']
    except Exception as e:
        gr.error(
            f"Error: {e}"
        )
    transciption


web = gr.Interface(
    fn=lambda x: x, 
    inputs=gr.Audio(
        sources=["microphone"], 
        type="filepath"
        ), 
    outputs=[],
    title= "Audio Transcription",
    description= "Transcribe audio from your microphone"
    )

web.launch(share=True)