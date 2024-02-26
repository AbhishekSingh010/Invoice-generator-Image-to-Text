# Invoice Reader - Image to Text

This is a Streamlit web application that utilizes Google's GenerativeAI API, specifically the Gemini model, to extract information from invoice images and convert it into text. It's designed to assist users in understanding invoice contents by providing responses based on the input image.

## How to Use:

1. **Input Prompt:**
   - Enter a description of the task or prompt related to understanding invoices. This will help guide the model's response.

2. **Choose an Image:**
   - Upload an image of an invoice in either JPG, JPEG, or PNG format.

3. **Click "Tell me about the image":**
   - Once both the input prompt and an image are provided, click this button to initiate the process.

4. **View Response:**
   - After processing, the application will display the extracted text information from the invoice image.

## Prerequisites:

- **Environment Variables:**
  - Make sure to set up a `.env` file with your Google API key stored as `GOOGLE_API_KEY`.

## How to Run Locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AbhishekSingh/invoice-reader.git

2. **Install Dependencies:**
   ```bash
   cd invoice-reader

3. **Set Environment Variables:**
Create a .env file in the root directory and add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_api_key_here


4.**Run the Application:**
Copy code
streamlit run app.py


5.**Access the Application:**
Once the application is running, open your web browser and go to the provided URL (typically http://localhost:8501).


  










