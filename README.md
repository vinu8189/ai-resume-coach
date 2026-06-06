# 💼 AI Resume Coach

An AI-powered tool that analyzes a resume against a job description and provides a match score, missing skills, and interview insights using LLMs.

---

## 🚀 Features

- Upload resume (PDF)
- Paste job description
- AI-based match analysis
- Skill gap detection
- Interview questions
- Improvement suggestions
- LangSmith tracing enabled

---

## 🧠 Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- LangSmith
- PyPDF

---

## 🏗️ Workflow

```text
Streamlit UI (Frontend)
   ↓
PDF Text Extraction
   ↓
Resume + Job Description
   ↓
LangChain Prompt
   ↓
Gemini LLM (AI Model)
   ↓
Structured Output
   ↓
Streamlit Display

LangSmith Tracking (Observability)

---

## 📸 Screenshots

### UI Landing Page

![UI](assets/ui.png)

### UI Input

![Input](assets/input.png)

### AI Analysis Output

![Output](assets/output.png)

### LangSmith Tracing

![LangSmith](assets/tracing.png)
