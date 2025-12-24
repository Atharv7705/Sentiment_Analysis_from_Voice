#  Sentiment Analysis from Voice

A machine learning project that records audio from the user, converts speech to text, and performs sentiment analysis using state-of-the-art NLP models. The system identifies whether the spoken input is Positive, Negative, or Neutral and displays a confidence score. Includes a Streamlit-based web frontend.

---

##  Features
- Voice recording from microphone  
- Speech-to-text using Google Web Speech API  
- Sentiment Analysis using HuggingFace Transformers  
- Confidence score output  
- Web-based UI using Streamlit  
- Lightweight and easy to deploy  

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python 3.10+
- SpeechRecognition  
- SoundDevice  
- SciPy  
- Transformers (HuggingFace)  
- PyTorch  

---

##  Project Structure

sentiment-analysis/

│

├── app.py # Streamlit frontend + backend logic

├── temp.wav # Temporary recorded audio file

├── requirements.txt

└── README.md


---

# ⚙️ Setup Instructions

Follow these steps to run the project smoothly.

---

setup_steps:
  - step: 1
    title: Clone the Repository
    commands:
      - git clone [https://github.com/atharvhalwai/Sentiment_Analysis_from_Voice.git](https://github.com/Atharv7705/Sentiment_Analysis_from_Voice.git)
      - cd sentiment-analysis

  - step: 2
    title: Create Virtual Environment
    commands:
      - python -m venv venv

  - step: 3
    title: Activate Virtual Environment
    commands:
      windows:
        - venv\Scripts\activate
      linux_mac:
        - source venv/bin/activate

  - step: 4
    title: Install Dependencies
    commands:
      - pip install --upgrade pip
      - pip install streamlit sounddevice scipy SpeechRecognition transformers==4.36.2 torch numpy requests

  - step: 5
    title: Run the Application
    commands:
      - python -m streamlit run app.py
## 📸 Output

Below is a sample output of the application:

<img width="1779" height="970" alt="Screenshot 2025-12-18 232551" src="https://github.com/user-attachments/assets/9404f2c6-bb71-4daf-9bc6-e59d5379e916" />




