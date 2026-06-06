# 💼 AI Resume Coach (LangChain + Gemini + LangSmith)

An AI-powered resume analyzer that compares a resume with a job description and generates structured insights like match score, missing skills, interview questions, and improvement suggestions.

Built as a learning project to explore **LLM applications, LangChain workflows, and observability with LangSmith**.

---

# 🚀 Features

- Upload resume (PDF)
- Paste job description
- AI-based resume vs job matching
- Skill gap detection
- Interview question generation
- Difficulty estimation
- Structured AI insights
- LangSmith tracing for debugging & observability

---

# 🧠 Tech Stack

- Python
- Streamlit (UI)
- LangChain
- Google Gemini API
- LangSmith (Observability)
- PyPDF (PDF text extraction)

---

# 🏗️ How it works

Streamlit UI  
↓  
PDF Extraction (PyPDF)  
↓  
Text + Job Description  
↓  
LangChain Prompt  
↓  
Gemini LLM  
↓  
Structured AI Response  
↓  
Streamlit Output  
↓ 
LangSmith tracks every step

---

# 📥 Input

### Resume
- PDF file uploaded via Streamlit

### Job Description
- Pasted as text input

---

# 📤 Output

The AI generates:

- Match score
- Strengths
- Missing skills
- Interview difficulty level
- Suggested interview questions
- Improvement recommendations

---

