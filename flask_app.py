from flask import Flask, request
import streamlit as st

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    # Save the file and update the session state
    file.save('uploaded.wav')
    st.session_state.audio_data = open('uploaded.wav', 'rb').read()
    
    return "File uploaded", 200

if __name__ == "__main__":
    app.run(port=8000)
