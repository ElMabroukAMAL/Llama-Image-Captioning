from functions.functions import encode_image
from functions.functions import generate_caption
import streamlit as st

# Streamlit App

st.set_page_config(page_title=" Image Captioning", page_icon="🤖")

# App title
st.title("Llama Captioner")

# file_uploader component allows users to select an image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
   # Show the uploaded image
   st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

   if st.button("Generate Caption"):
       with st.spinner("Generating caption..."):
           caption = generate_caption(uploaded_file)
       st.success("Caption Generated!")
       st.write("**Caption:**", caption)
