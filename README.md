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
Streamlit UI (Front end)
   ↓
PDF Text Extraction
   ↓
Resume + Job Description
   ↓
LangChain Prompt
   ↓
Gemini LLM (AI model)
   ↓
Structured Output
   ↓
Streamlit Display

+ LangSmith tracking (Observability)

---

## 📸 Screenshots

### UI Landing page
![UI](assets/ui.png)

### UI Input
![UI](assets/input.png)

### AI Analysis Output
![Result](assets/output.png)

### LangSmith Tracing
![LangSmith](assets/tracing.png)
