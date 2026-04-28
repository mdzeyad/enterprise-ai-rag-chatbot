```python
import streamlit as st

st.title("🤖 Enterprise AI Chatbot (RAG Demo)")

st.write("Upload your document and ask questions (demo version)")

uploaded_file = st.file_uploader("Upload PDF or Text file")

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    question = st.text_input("Ask a question from document:")

    if question:
        st.write("🤖 Answer:")
        st.write("This is a demo response. In full version, LLM + FAISS will generate real answers.")
```
