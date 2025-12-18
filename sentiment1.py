import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write
from transformers import pipeline

# Audio settings
fs = 16000  # Sample rate
seconds = 5

print("Speak now...")
audio_data = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1,
    dtype='int16'   # 🔥 FIX: record as PCM int16
)
sd.wait()

# Save WAV in correct PCM format
write("temp.wav", fs, audio_data)

# Speech Recognition
recognizer = sr.Recognizer()
with sr.AudioFile("temp.wav") as source:
    audio = recognizer.record(source)

text = recognizer.recognize_google(audio)
print("Recognized Text:", text)

# Sentiment Analysis
sentiment_pipeline = pipeline("sentiment-analysis")
result = sentiment_pipeline(text)[0]

print("Sentiment:", result["label"])
print("Confidence:", round(result["score"] * 100, 2), "%")
