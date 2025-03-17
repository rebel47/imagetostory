import os
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from gtts import gTTS
import google.generativeai as genai
import streamlit as st
from PIL import Image  # Add this import statement

# Load environment variables
load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Image to text using Google Gemini API
def img2text(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        
        input_prompt = "Describe the content of the image in very detail and concise way not more than 100 words"
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content([input_prompt, image_parts[0]])
        text = response.text
        return text
    else:
        raise FileNotFoundError("No file uploaded")

# Generate story
def generate_story(scenario):
    input_prompt = f'''
    You are a storyteller;
    You can generate a short story based on a the given narrative, try to be more realistics and the story should be no more than 300 words;
    CONTEXT: {scenario}
    STORY: 
    '''
    model = genai.GenerativeModel('gemini-1.5-flash')
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
    st.text("       - Developed By: Mohammad Ayaz Alam")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_container_width =True)

    if st.button("Generate Story"):
        if uploaded_file is not None:
            # Convert image to text
            scenario = img2text(uploaded_file)
            st.write(f"**Extracted Text:** {scenario}")

            # Generate story
            story = generate_story(scenario)
            st.write(f"**Generated Story:** {story}")

            # Convert story to speech
            audio_file = text2speech(story)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("Please upload an image first")

if __name__ == '__main__':
    main()
