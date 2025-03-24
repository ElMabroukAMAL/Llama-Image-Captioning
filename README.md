## Project Overview

This web application leverages **Artificial Intelligence** to analyze an image, generate a textual description, and convert it into speech. It provides a seamless way to "hear" what's in an image using cutting-edge AI models.

### How It Works

1. 📸 **Upload an Image** – Users can upload a `.jpg`, `.jpeg`, or `.png` file through the Streamlit web interface.
2. 📝 **Generate a Caption** – The app processes the image using ` Llama-3.2-90b-Vision` via the ` Groq API` to generate an accurate textual description.
3. 🔊 **Convert to Speech** – The generated caption is then converted into spoken audio using ` Hugging Face’s ESPnet model`.
