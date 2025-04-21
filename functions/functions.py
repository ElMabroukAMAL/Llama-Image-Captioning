from groq import Groq
import base64
import os
import json
import requests

# Set up Groq API Key
os.environ['GROQ_API_KEY'] = json.load(open('credentials.json', 'r'))['groq_token']
# Set up HUGGINGFACE API Key
HUGGINGFACE_API_TOKEN= json.load(open('credentials.json', 'r'))['HUGGINGFACE_API_TOKEN']

# Function to encode the image from local file
def encode_image(image_path):
   with open(image_path, "rb") as image_file:
       return base64.b64encode(image_file.read()).decode('utf-8')
   

# Function to generate caption
def generate_caption(uploaded_image):
   base64_image = base64.b64encode(uploaded_image.read()).decode('utf-8')

   # client is used to interact with a service that can process the image and generate a caption
   client = Groq()

   # send a request to the model. The request includes a message with two parts:
   #      1. A text prompt asking, "What's in this image?"
   #      2. The base64-encoded image itself, formatted as a data URL.
   #      3. the model
   chat_completion = client.chat.completions.create(
       messages=[
           {
               "role": "user",
               "content": [
                   {"type": "text", "text": "What's in this image?"},
                   {
                       "type": "image_url",
                       "image_url": {
                           "url": f"data:image/jpeg;base64,{base64_image}",
                       },
                   },
               ],
           }
       ],
       model="llama-3.2-90b-vision-preview",
   )
   return chat_completion.choices[0].message.content


def generate_speech_from_text(message):
    """
    Uses HuggingFace's ESPnet text-to-speech model to generate audio from a text (message).
    Sends a POST request with the input text to the HuggingFace API and saves the response as a .flac audio file.
    """
    API_URL = "https://router.huggingface.co/hf-inference/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payloads = {
        "inputs": message
    }
    response = requests.post(API_URL, headers=headers, json=payloads)
    with open("generated_audio.flac", "wb") as file:
        file.write(response.content)
