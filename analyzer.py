# analyzer.py
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are a senior technical recruiter.

Resume:
{resume}

Job Description:
{job_description}

Provide:

1. Match Score (0-100)
2. Key Strengths
3. Missing Skills
4. Interview Difficulty
5. Five Interview Questions
6. Resume Improvement Suggestions
""")

chain = prompt | llm

def analyze(resume_text, jd_text):
    return chain.invoke({
        "resume": resume_text,
        "job_description": jd_text
    })