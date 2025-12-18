\# 🎤 Sentiment Analysis from Voice  

A machine learning project that records a user's voice, converts the speech into text, and performs sentiment analysis to determine whether the user sounds Positive, Negative, or Neutral.  



---



\## 🚀 Features

\- 🎙 Voice recording (via microphone)

\- 🔊 Audio-to-text conversion using Google Speech Recognition

\- 🤖 Sentiment classification using HuggingFace Transformers

\- 📊 Confidence score output

\- 🖥 Streamlit-based web frontend

\- 🗄 Optional database storage for logs (SQLite)



---



\## 🧠 Project Architecture



\*\*Voice Input → WAV File → Speech Recognition → Text → Sentiment Model → Output\*\*



---



\## 🛠 Tech Stack



\### \*\*Frontend\*\*

\- Streamlit (Python Web UI)



\### \*\*Backend\*\*

\- Python 3.10+

\- Transformers (HuggingFace)

\- Torch

\- SpeechRecognition

\- SoundDevice

\- SciPy



\### \*\*APIs / Models\*\*

\- Google Web Speech API (for speech-to-text)

\- HuggingFace Transformers pipeline (for sentiment analysis)



\### \*\*Database (Optional)\*\*

\- SQLite (local)

\- SQLAlchemy (ORM)



---



\## 📦 Folder Structure



sentiment-analysis/

│

├── app.py # Streamlit frontend

├── sentiment\_core.py # Backend logic (optional)

├── temp.wav # Temporary audio file

├── requirements.txt

├── database.db # SQLite DB (optional)

└── README.md

