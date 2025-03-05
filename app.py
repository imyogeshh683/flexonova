import streamlit as st
import requests

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

# Function to generate text
def generate_text(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']

# Streamlit app
st.title("MentalX")
st.write("Generate captions, hashtags, and post ideas in seconds!")

# User input
prompt = st.text_input("What's your post about? (e.g., 'A new coffee shop opening')")

if st.button("Generate"):
    if prompt:
        output = generate_text(f"Generate 5 social media captions and hashtags for: {prompt}")
        st.write(output)
    else:
        st.write("Please enter a topic!")