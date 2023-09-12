import openai
import streamlit as st

# Set your OpenAI API key here
openai.api_key = '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'

# Streamlit app title
st.title("Meeting Minutes Generator")

# Input for meeting notes
meeting_notes = st.text_area("Enter Meeting Notes", "")

# Number of minutes to generate
num_minutes = st.number_input("Number of Minutes to Generate", min_value=1, max_value=10, value=1)

if st.button("Generate Minutes"):
    if meeting_notes:
        # Function to generate meeting minutes
        def generate_meeting_minutes(meeting_notes, num_minutes):
            minutes = []
            for _ in range(num_minutes):
                prompt = f"Generate meeting minutes from the following notes:\n{meeting_notes}\nMinutes:"
                
                response = openai.Completion.create(
                    engine="davinci",
                    prompt=prompt,
                    max_tokens=150,  # Adjust the length of the response as needed
                    n=1,  # Generate a single response
                    stop=None,  # You can specify stop conditions if needed
                    temperature=0.7,  # Adjust temperature for creativity
                )
                
                generated_minutes = response.choices[0].text.strip()
                minutes.append(generated_minutes)
            return minutes

        # Generate and display meeting minutes
        generated_minutes = generate_meeting_minutes(meeting_notes, num_minutes)
        st.subheader("Generated Meeting Minutes:")
        for i, minute in enumerate(generated_minutes, start=1):
            st.write(f"Minute {i}:\n{minute}")
    else:
        st.warning("Please enter meeting notes.")
