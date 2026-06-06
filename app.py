import streamlit as st
from analyzer import analyze
from utils import extract_pdf_text

st.title("AI Resume Coach")

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze"):

    resume_text = extract_pdf_text(resume_file)

    response = analyze(
        resume_text,
        jd
    )

    st.write(response.content)