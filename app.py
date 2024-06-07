import os
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from gtts import gTTS
import google.generativeai as genai
import streamlit as st

# Load environment variables
load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Image to text
def img2text(file_path):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(file_path)[0]["generated_text"]
    return text

# Generate story
def generate_story(scenario):
    input_prompt = f'''
    You are a story teller;
    You can generate a short story based on a simple narrative, the story should be no more than 50 words;
    CONTEXT: {scenario}
    STORY: 
    '''
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

# Text to speech
def text2speech(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    return filename

# Streamlit app
def main():
    st.title("AI Story Generator from Image")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp"])
    if uploaded_file is not None:
        # Save the uploaded file to disk
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Story"):
            # Convert image to text
            scenario = img2text(uploaded_file.name)
            st.write(f"Extracted Text: {scenario}")

            # Generate story
            story = generate_story(scenario)
            st.write(f"Generated Story: {story}")

            # Convert story to speech
            audio_file = text2speech(story)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")

if __name__ == '__main__':
    main()