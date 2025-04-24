import streamlit as st
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

# Language mapping
languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "German": "de"
}

# Translator
translator = Translator()

# Text-to-speech
def speak_text(text, select_language):
    tts = gTTS(text=text, lang=select_language)
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    mp3.seek(0)
    return mp3

# Translate using googletrans
def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Page Config
st.set_page_config(page_title="Visual AI Bot", layout="centered")

# Custom CSS using named colors
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: lavender;
    }

    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 16px lightgray;
    }

    h1 {
        color: royalblue;
        text-align: center;
    }

    .stTextArea > div > textarea {
        background-color: aliceblue;
        border-radius: 10px;
        padding: 10px;
        color: black;
    }

    .stSelectbox {
        background-color: aliceblue;
        border-radius: 10px;
    }

    .stButton > button {
        background-color: royalblue;
        color: white;
        padding: 0.5em 1.5em;
        font-size: 1em;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        margin-top: 10px;
        transition: background 0.3s;
    }

    .stButton > button:hover {
        background-color: mediumblue;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# App UI
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🎙️ Visual AI Bot")
st.markdown("Translate and speak your English in multiple languages: **English**, **Urdu**, **Arabic**, **German**.")

text_input = st.text_area("✍️ Enter text in English", placeholder="e.g., My name is Shoaib")
selected_language = st.selectbox("🌐 Select language to speak", list(languages.keys()))

if st.button("🗣️ Translate & Speak"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            select_language = languages[selected_language]
            translated = translate_text(text_input, select_language)
            st.success(f"✅ Translated to {selected_language}:")
            st.markdown(f"**📝 {translated}**")

            audio = speak_text(translated, select_language)
            st.audio(audio, format='audio/mp3')
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
