import streamlit as st
import tempfile

from src.pdf_loader import load_pdf
from src.vector_store import create_vector_store
from src.rag_chain import ask_question

st.title("RAG PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())

        pdf_path = tmp.name

    chunks = load_pdf(pdf_path)

    db = create_vector_store(chunks)

    question = st.text_input(
        "Ask a question"
    )

    if question:

        answer = ask_question(
            db,
            question
        )

        st.write(answer)