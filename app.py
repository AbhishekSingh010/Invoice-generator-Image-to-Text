from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input_prompt, image_data, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input_prompt, image_data[0], prompt])
    return response.text

# Function to load image details
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")



# Set page config and title
st.set_page_config(page_title="Invoice reader - Image to Text")


# # Header
# st.markdown("<h1 style='text-align: center; font-family: serif;'>Gemini Application</h1>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align: center;'>Extract information from invoice images</h3>", unsafe_allow_html=True)

# Input prompt and image upload
input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices &
you will have to answer questions based on the input image
"""
input_prompt = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Process extraction upon clicking the button
if st.button("Tell me about the image"):
    # Check if file is uploaded
    if uploaded_file is None:
        st.error("Please upload an image.")
    else:
        try:
            # Process image data
            image_data = input_image_setup(uploaded_file)
            # Get Gemini response
            with st.spinner("Processing..."):
                response = get_gemini_response(input_prompt, image_data, input_prompt)
                # Display response
                st.subheader("The Response is")
                st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
