import streamlit as st
import fitz  # PyMuPDF
import requests

st.title("📄 Document Summarization Tool")

uploaded_file = st.file_uploader("Upload a PDF Document", type=["pdf"])

if uploaded_file is not None:
    # Extract text
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    st.subheader("📃 Extracted Text")
    st.text_area("Document Text", text[:1000] + "...", height=200)  # show preview
    
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            # Send request to local LLM
            res = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "mistral",
                    "prompt": f"Summarize the following document:\n{text}",
                    "stream": False
                }
            )
            summary = res.json()["response"]
            st.subheader("📝 Summary")
            st.success(summary)
