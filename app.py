import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from PIL import Image # Importing the Pillow library for image processing 


st.set_page_config(page_title="Defect Recognition", page_icon="🤖", layout="wide")
st.title("🔬AI-Powered Defect Recognition Suite :blue[Powered by Google Generative AI]✨")
st.subheader("⚙️:blue[Prototype for automated structural defect recognition]")
st.markdown("This application uses Google Generative AI to analyze defects in images. Upload an image and get insights on the defects present in it.")

with st.expander("About the Application", expanded=True, icon="ℹ️"):
    st.markdown("""
    This application is designed to demonstrate the capabilities of Google Generative AI in recognizing and analyzing defects in images. It allows users to upload an image, which is then processed to identify any defects present. The application provides a user-friendly interface for interacting with the AI model.
    - **Defect Detecttion**: Automatically detects and analyzes defects in uploaded images.
    - **Recommendations**: Provides recommendations based on the detected defects.
    - **Report Generation**: Generates a report summarizing the analysis and recommendations.
    """)

    
key = os.getenv('Google_API_Key')
genai.configure(api_key=key)



st.subheader("Upload an Image for Analysis")
with st.sidebar:
    st.title("📄 App Info")
    st.info(" A prototype app to automatically detect and analyze structural defects in images using AI", icon="🤖")
    # Using an expander for a cleaner look
    with st.expander("👤 About the Creator"):
        st.markdown("""
        **Created by:**             
        [Kumara Vijay M G]
        
        Feel free to connect for further details or collab opportunities!
        
     ---
        
        📧 **Email:** [Kumaravijay2626@gmail.com](mailto:kumaravijay2626@gmail.com)
        
        🔗 **LinkedIn:** [linkedin.com/in/Kumaravijay](https://www.linkedin.com/in/kumara-vijay-m-g-71a639317/)
        
        🐙 **GitHub:** [github.com/Kumaravijay](https://github.com/Kumaravija)
        """)
input_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if input_image:
    img = Image.open(input_image)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
if st.button("Analyze Image", type="primary"):
    with st.spinner("Analyzing the image..."):
        try:
            prompt = f""" You are an expert in defect recognition and analysis. Say what are all the things present in the image and Analyze the uploaded image for any defects and provide a detailed report on the findings. Include recommendations for addressing the identified defects. Find the evidence of defects in the image and provide a comprehensive analysis. provide a report summarizing the analysis and recommendations. I need finite details for the image and give in points in a understandable manner. Categories the image into different types of defects and provide a detailed report on each category. Categories are less than 5 defects, more than 5 defects, and no defects. Provide a detailed report on the analysis and recommendations. """
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content([prompt,img])
            st.write(response.text)
        except Exception as e:
            st.error(f"Error in processing the image: {e}")


    
    
