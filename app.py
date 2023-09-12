import openai
import streamlit as st

# Set your OpenAI API key here
openai.api_key = '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'

st.title('GPT-3 Chat')
st.write('Chat with OpenAI\'s GPT-3')

# Text input for the user to enter a message
user_input = st.text_input('You:')

# Button to send the message and get a response
if st.button('Send'):
    # Get a response from GPT-3
    response = openai.Completion.create(
        engine='davinci',
        prompt=f'You: {user_input}\nGPT-3:',
        temperature=0.7,
        max_tokens=150
    )
    # Get the GPT-3 response text
    gpt3_response = response.choices[0].text.strip()
    
    # Display the GPT-3 response
    st.write(f'GPT-3: {gpt3_response}')


