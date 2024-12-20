# AI Story Generator from Image 📖🖼️

AI Story Generator from Image is a Streamlit-based web application that leverages Google Gemini API and Hugging Face's Transformers to extract text from images, generate creative short stories, and convert them to speech. It's an all-in-one storytelling assistant designed to bring your images to life with engaging narratives.

## Features
- **Image to Text:** Extract detailed and concise descriptions from uploaded images using the Google Gemini API.
- **Story Generation:** Create short, realistic, and engaging stories based on the extracted text using AI-powered models.
- **Text-to-Speech Conversion:** Convert the generated story into audio for an immersive storytelling experience.

## Live Demo
Try the app here: [AI Story Generator from Image](https://scenescripter.streamlit.app/)

## Installation

### Prerequisites
- Python 3.8 or above
- API keys for:
  - Google Gemini API
  - Hugging Face Transformers

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rebel47/ai-story-generator.git
   cd ai-story-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   GOOGLE_API_KEY=your_google_api_key
   HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_api_token
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## How It Works
1. **Upload an Image:** Start by uploading an image in any supported format (e.g., JPG, PNG, GIF, BMP, WEBP).
2. **Text Extraction:** The app uses the Google Gemini API to extract concise textual descriptions from the image.
3. **Story Creation:** Based on the extracted text, the app generates a short story (no more than 300 words) using AI models.
4. **Listen to the Story:** The generated story is converted to speech and can be played directly within the app.

## Example Workflow
1. Upload an image of a serene forest.
2. Extracted Text: *"A dense forest with sunlight filtering through the trees and a small wooden cabin in the distance."*
3. Generated Story: *"Once upon a time, in a dense forest, a young artist found inspiration in a wooden cabin surrounded by nature's beauty..."*
4. Listen to the story in an engaging audio format.

## Supported Formats
- Image formats: JPG, JPEG, PNG, GIF, BMP, TIFF, TIF, WEBP

## Technologies Used
- **Streamlit:** For the web application interface
- **Google Gemini API:** For advanced image-to-text processing
- **Hugging Face Transformers:** For generating creative narratives
- **gTTS (Google Text-to-Speech):** For audio conversion of the stories
- **Pillow:** For image handling and display

## Future Enhancements
- Add support for additional languages in text-to-speech conversion.
- Enable customization of storytelling styles (e.g., humorous, dramatic, poetic).
- Incorporate offline mode for basic text extraction and story generation.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- **Google Cloud:** For their cutting-edge APIs
- **Hugging Face:** For state-of-the-art NLP models
- **Streamlit:** For enabling rapid application development

---

**Developed with ❤️ by Mohammad Ayaz Alam**
```
