from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
#import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini with API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
from google import genai

client = genai.Client(api_key="AIzaSyCTKSTK6wmKfNrdSWSe_CUYKro7uahKbTE")



# Function to format text as markdown blockquote
def to_markdown(text):
    text = text.replace('•', '  *')  # bullet formatting
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Function to get Gemini response
def get_gemini_response(question):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=question
    )
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("💬 Gemini Application")

# Input field
user_input = st.text_input("Input your question:", key="input")

# Button to submit question
submit = st.button("Ask the Question")

# When button is clicked
if submit and user_input:
    response = get_gemini_response(user_input)
    st.subheader("🧠 The Response is:")
    st.markdown(to_markdown(response))