import streamlit as st
import openai

# Set up OpenAI API Key
openai.api_key = "YOUR_API_KEY"  # Replace with your actual OpenAI key

st.set_page_config(page_title="AI Support Assistant", page_icon="💬", layout="wide")

# Custom Styling for full page width and longer layout
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 5rem;
            max-width: 1000px;
            margin: auto;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 12px;
        }
        .stButton>button {
            background-color: #4B8BBE;
            color: white;
            padding: 10px 24px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center; padding: 10px 0;'>
        <h1 style='color: #4B8BBE;'>🤖 AI Customer Support Assistant</h1>
        <p style='font-size:18px;'>Instantly get answers to your support queries.</p>
    </div>
""", unsafe_allow_html=True)

# Input area
with st.form(key="chat_form"):
    user_query = st.text_input("Type your question below 👇", placeholder="e.g. How can I reset my password?")
    submit = st.form_submit_button("🔍 Get Answer")

# Response
if submit and user_query:
    with st.spinner("Generating answer..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support agent."},
                {"role": "user", "content": user_query}
            ]
        )
        ai_reply = response["choices"][0]["message"]["content"].strip()
        st.success("✅ AI Response:")
        st.markdown(f"<div style='background-color:#f0f2f6;padding:15px;border-radius:10px;font-size:16px;'>{ai_reply}</div>", unsafe_allow_html=True)

# Suggestions
with st.expander("💡 Need Suggestions?"):
    st.write("Try asking:")
    st.button("🔑 How do I change my password?")
    st.button("📦 Where is my order?")
    st.button("🕒 What are your working hours?")

# Footer
st.markdown("""
    <div style='text-align: center; padding-top: 50px;'>
        <hr style='margin-top: 40px; margin-bottom: 10px;'>
        <p style='font-size: 16px; color: gray;'>
            🚀 Built with ❤️ by <strong style='color:#4B8BBE;'>Sakshi Kotur</strong> | © 2025
        </p>
    </div>
""", unsafe_allow_html=True)
