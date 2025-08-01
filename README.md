# 🔬 AI-Powered Defect Recognition Suite

This project is a Streamlit web application that serves as a prototype for an AI-powered defect recognition system. It leverages the Google Generative AI API (specifically the Gemini Pro Vision model) to analyze user-uploaded images of industrial components or structures, identify potential defects, and provide a detailed report.
#### web App Link : https://defect-recognition-kumara-vijay.streamlit.app/

![App Screenshot](https://ibb.co/8L169Q7q).

---

## ✨ Key Features

* **Image Upload**: Users can easily upload images in common formats (`.jpg`, `.jpeg`, `.png`).
* **AI-Powered Analysis**: Utilizes Google's `gemini-pro-vision` model to perform advanced visual analysis.
* **Defect Detection**: Automatically identifies and describes various types of potential defects in the uploaded image.
* **Recommendations**: Provides actionable recommendations for addressing the identified issues.
* **Report Generation**: Generates a clear, user-friendly report summarizing the findings.

---

## 🛠️ Technology Stack

* **Backend**: Python
* **Web Framework**: Streamlit
* **AI/ML**: Google Generative AI (Gemini Pro Vision)
* **Image Processing**: Pillow
* **Environment Management**: python-dotenv

---

## 🚀 Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

* Python 3.8 or higher
* A Google AI API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/defect-recognition-suite.git](https://github.com/your-username/defect-recognition-suite.git)
cd defect-recognition-suite

3. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
Create a file named requirements.txt in the project's root directory and add the following lines:

streamlit
google-generativeai
python-dotenv
Pillow

Now, install these packages using pip:

pip install -r requirements.txt

5. Configure Environment Variables
Create a file named .env in the project's root directory. This file will store your secret API key. Do not commit this file to version control.

Open the .env file and add your Google API Key like this:

# .env file
GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Replace "YOUR_API_KEY_HERE" with your actual key.

▶️ How to Run the Application
Once you have completed the setup, you can run the Streamlit application with a single command:

streamlit run app.py

Your web browser should automatically open to the application's URL (usually http://localhost:8501).

📁 Project Structure
Here is the recommended file structure for your project:

defect-recognition-suite/
│
├── .env                # Stores your secret API key
├── app.py              # The main Streamlit application script
├── requirements.txt    # Lists the Python dependencies
└── README.md           # This file
