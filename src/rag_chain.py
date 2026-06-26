import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load local .env (only used on your laptop)
load_dotenv()

# Read API key
api_key = None

# First try Streamlit Secrets
try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

# If not found, use local .env
if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

# Stop immediately if no key is found
if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Add it to Streamlit Secrets or your local .env file."
    )

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0,
)


def ask_question(db, question):
    docs = db.similarity_search(question, k=4)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content