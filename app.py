import streamlit as st

st.title("RAG PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:
    st.success("PDF uploaded successfully!")

question = st.text_input(
    "Ask a question"
)

if question:
    st.write("Answer will appear here")