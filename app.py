from functions.functions import encode_image, generate_caption, generate_speech_from_text
import streamlit as st

def main():

    # Streamlit App

    st.set_page_config(page_title=" Image Captioning", page_icon="🤖")

    # App title
    st.title("Llama Captioner")

    # file_uploader component allows users to select an image file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Show the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Store caption in session state
        if "caption" not in st.session_state:
            st.session_state.caption = ""

        # Generate Caption
        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                st.session_state.caption = generate_caption(uploaded_file)
            st.success("Caption Generated!")
        if st.session_state.caption:
            st.write("**Caption:**", st.session_state.caption)

        # Generate Audio (Only show if caption exists)
        if st.session_state.caption:
            if st.button("Generate Audio"):
                with st.spinner("Generating audio..."):
                    audio = generate_speech_from_text(st.session_state.caption)
                st.success("Audio Generated!")
                st.audio("generated_audio.flac")

if __name__ == "__main__":
    main()