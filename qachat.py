from dotenv import load_dotenv
import streamlit as st
import os
from google import genai

# Load environment variables
load_dotenv()

# Configure Gemini API using new Client interface
client = genai.Client(api_key=os.getenv("AIzaSyBNjCaVcTXFUwRtgv1tsAEDpmSSpYETaes"))
model_name = "gemini-2.0-flash"  # Correct model path for 2.0 flash

# Streamlit app setup
st.set_page_config(page_title="Gemini 2.0 Chatbot", page_icon="🤖")
st.title("🤖 Gemini 2.0 Flash Chatbot")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input box
user_input = st.text_input("Ask your question:", key="input")
submit = st.button("Send")

# On submit
if submit and user_input:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[{"role": "user", "parts": [{"text": user_input}]}]
        )
        gemini_reply = response.text

        # Save to chat history
        st.session_state['chat_history'].append(("user", user_input))
        st.session_state['chat_history'].append(("bot", gemini_reply))

    except Exception as e:
        st.error(f"⚠ Error: {e}")

# Show chat history
st.markdown("### 💬 Chat History")
for role, text in st.session_state['chat_history']:
    if role == "user":
        st.markdown(
            f"""
            <div style='background-color:#DCF8C6; padding:10px; border-radius:10px; margin:10px 0;'>
                <b>You:</b> {text}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <div style='background-color:#F1F0F0; padding:10px; border-radius:10px; margin:10px 0;'>
                <b>Gemini:</b> {text}
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<center><small>🤝 Contributed by Avi.</small></center>", unsafe_allow_html=True)