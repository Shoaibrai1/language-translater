import streamlit as st
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

#  Language 
languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "German": "de"
}

# Initialize translator
translator = Translator()


def speak_text(text, select_language):
    tts = gTTS(text=text, lang=select_language)
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    return mp3

#  Translate using googletrans
def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation.text

#  Streamlit UI
st.set_page_config(page_title="Visual AI Bot", layout="centered")
st.title(" Visual AI Bot ")

st.markdown("Translate and speak your English language in multiple languages: **English**, **Urdu**, **Arabic**, **German**.")

text_input = st.text_area(" Enter text in English", placeholder="e.g., My name is Shoaib")

selected_language = st.selectbox(" Select language to speak", list(languages.keys()))

if st.button(" Translate & Speak"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        try:
            select_language = languages[selected_language]
            translated = translate_text(text_input, select_language)
            st.success(f" Translated to {selected_language}:")
            st.markdown(f"**{translated}**")

            audio = speak_text(translated, select_language)
            st.audio(audio, format='audio/mp3')
        except Exception as e:
            st.error(f" Error: {e}") 
