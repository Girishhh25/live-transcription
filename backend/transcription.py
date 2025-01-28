import whisper
import sounddevice as sd
import requests
import numpy as np


# Load Whisper model
model = whisper.load_model("base")

# Flask server endpoint
SERVER_URL = "http://127.0.0.1:5000/transcribe"

# Define sample rate for audio recording
SAMPLE_RATE = 16000 

# Callback function for audio processing
def audio_callback(indata, frames, time,status):
    if status:
        print(f"Status: {status}")
    audio = np.frombuffer(indata, dtype=np.float32)
    # Perform real-time transcription
    result = model.transcribe(audio, fp16=False)
    transcribed_text = result.get('text', '').strip()
    print(transcribed_text)
    # Send transcription to server
    requests.post(SERVER_URL, json={"text": transcribed_text})

# Start real-time audio capture
def start_transcription():
    print("Starting audio transcription...")
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE):
        input("Press Enter to stop...\n")

if __name__ == "__main__":
    start_transcription()
