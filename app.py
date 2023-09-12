import os
import openai
import streamlit as st

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Load the HTML file
with open('audio_recorder.html', 'r') as file:
    html = file.read()

# Embed the HTML in the Streamlit app
st.components.v1.html(html, height=600)

# Check if audio data has been received
if "audio_data" in st.session_state:
    # Your processing code here (e.g., send the audio data to OpenAI's API)
    st.audio(st.session_state.audio_data, format='audio/wav')
