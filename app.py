import streamlit as st
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analysis from Voice", layout="centered")

st.title("🎤 Sentiment Analysis from Voice")
st.write("Speak and detect emotion from your voice")

# Audio settings
fs = 16000
seconds = 5

if st.button("🎙 Record Voice"):
    st.info("Recording... Please speak")
    device_index = 1  # <- update this

    audio = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype='int16',
        device=device_index
    )
    sd.wait()
    
    write("temp.wav", fs, audio)
    st.success("Recording completed")

    # Speech Recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.subheader("📝 Recognized Text")
        st.write(text)

        # Sentiment Analysis
        sentiment_pipeline = pipeline("sentiment-analysis")
        result = sentiment_pipeline(text)[0]

        st.subheader("📊 Sentiment Result")
        st.write(f"**Sentiment:** {result['label']}")
        st.write(f"**Confidence:** {round(result['score'] * 100, 2)} %")

    except Exception as e:
        st.error("Could not recognize speech")
