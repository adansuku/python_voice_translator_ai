import gradio as gr

def tanslator(audio_file)
    

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