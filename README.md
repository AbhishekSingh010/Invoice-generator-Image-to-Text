# Invoice-generator-Image-to-Text

Invoice Reader - Image to Text
This is a Streamlit web application that utilizes Google's GenerativeAI API, specifically the Gemini model, to extract information from invoice images and convert it into text. It's designed to assist users in understanding invoice contents by providing responses based on the input image.

How to Use:
Input Prompt:

Enter a description of the task or prompt related to understanding invoices. This will help guide the model's response.
Choose an Image:

Upload an image of an invoice in either JPG, JPEG, or PNG format.
Click "Tell me about the image":

Once both the input prompt and an image are provided, click this button to initiate the process.
View Response:

After processing, the application will display the extracted text information from the invoice image.
Prerequisites:
Environment Variables:
Make sure to set up a .env file with your Google API key stored as GOOGLE_API_KEY.
How to Run Locally:
Clone the Repository:

bash
Copy code
git clone https://github.com/AbhishekSingh010/invoice-reader.git
Install Dependencies:

bash
Copy code
cd invoice-reader
pip install -r requirements.txt
Set Environment Variables:

Create a .env file in the root directory and add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_api_key_here
Run the Application:

bash
Copy code
streamlit run app.py
Access the Application:

Once the application is running, open your web browser and go to the provided URL (typically http://localhost:8501).
Contributors:
Your Name
License:
This project is licensed under the MIT License.
Feel free to contribute to this project by forking and submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Thank you for using Invoice Reader
