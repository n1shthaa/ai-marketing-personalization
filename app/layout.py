import streamlit as st

def show_homepage():
    st.subheader("📌 Project Overview")
    st.markdown("""
    This app uses AI to:
    - 🔍 Segment customers
    - 🎯 Recommend personalized offers
    - 📈 Predict conversion probability
    - 💬 Generate NLP-based marketing messages

    Data is backed by a PostgreSQL database, and models will be plugged in progressively.
    """)
