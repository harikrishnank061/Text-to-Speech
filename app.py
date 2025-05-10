import streamlit as st
from gtts import gTTS
import cohere
import os

# Function to convert text to speech using gTTS
def text_to_speech(text, lang='en', slow=False):
    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=lang, slow=slow)
        
        # Save the speech to a file
        file_path = "output.mp3"
        tts.save(file_path)
        
        return file_path
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Streamlit app layout
st.set_page_config(page_title="Text-to-Speech using gTTS and Cohere", page_icon="🔊")
st.title("🔊 Text-to-Speech using gTTS and Cohere")
st.markdown("Convert text to speech using the gTTS API.")

# Input API key directly in the app (this is where you enter your Cohere API key)
api_key = st.text_input("Enter your Cohere API Key", type="password")

# Show a warning if the API key is not provided
if not api_key:
    st.warning("⚠️ Please enter your Cohere API key to proceed.")

# Input field for the text to convert to speech
text = st.text_area("Enter the text you want to convert to speech", height=200)

# Options for speech
lang = st.selectbox("Language", ["en", "es", "fr", "de", "it"], index=0)
slow = st.checkbox("Slow Speech", value=False)

# Button to trigger text-to-speech conversion
if st.button("Convert to Speech"):
    if api_key and text.strip():
        # Convert the text to speech using gTTS
        file_path = text_to_speech(text, lang=lang, slow=slow)
        if file_path:
            st.audio(file_path)
            st.success("✅ Speech synthesis successful!")
        else:
            st.error("Error converting text to speech.")
    else:
        st.warning("⚠️ Please provide both the API key and the text to convert.")

st.markdown("---")
st.caption("Powered by Cohere and gTTS | Built with ❤️ using Streamlit")
