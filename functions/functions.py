from groq import Groq
import base64
import os
import json

# Set up Groq API Key
os.environ['GROQ_API_KEY'] = json.load(open('credentials.json', 'r'))['groq_token']

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