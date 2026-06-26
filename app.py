import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from src.pdf_loader import load_pdf
from src.vector_store import create_vector_store
from src.rag_chain import ask_question

load_dotenv()

st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="📄"
)

st.title("📄 RAG PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    with st.spinner("Creating vector database..."):

        chunks = load_pdf(pdf_path)

        db = create_vector_store(chunks)

    st.success("PDF Indexed Successfully!")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        with st.spinner("Thinking..."):

            answer = ask_question(
                db,
                question
            )

        st.markdown("### Answer")

        st.write(answer)