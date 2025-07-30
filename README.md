# 🧠 LLM-Based Document Intelligence System

A powerful AI-driven system that processes natural language queries and retrieves decision-making insights from unstructured documents such as insurance policies, contracts, and emails — using Google Gemini API.

## 🚀 Features

- 🔍 Understands vague or incomplete user queries in plain English
- 📄 Parses PDF/Word/Email documents to extract policy clauses
- 🤖 Uses Gemini LLM to perform semantic search and clause reasoning
- 🧾 Outputs structured JSON with decision (e.g., approval), payout amount, and referenced policy clauses
- 🧠 Enables explainable AI for insurance, HR, legal, and compliance domains

---

## 🛠️ Tech Stack

- **Python 3**
- **Google Gemini API (LLM)**
- **LangChain** for LLM orchestration
- **PyMuPDF / pdfplumber** for PDF parsing
- **FAISS / SentenceTransformers** for semantic search
- **dotenv** for environment variable management

---

## 📥 Sample Query

```text
46-year-old male, knee surgery in Pune, 3-month-old insurance policy
