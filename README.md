# 🧬 Blood Test Analyser (Debugged & Functional)

This project is a humorous, AI-powered system that analyzes blood test PDFs and returns creative, sometimes questionable medical feedback using FastAPI, CrewAI, LangChain, and Gemini Pro.

---

## 🐞 Bugs Found & How They Were Fixed

| File | Bug | Fix |
|------|-----|-----|
| `main.py` | ❌ `ModuleNotFoundError: crewai`<br>❌ Uvicorn not starting | ✅ Added missing packages in `newreq.txt`<br>✅ Installed via `pip install -r newreq.txt` |
| `tools.py` | ❌ `read_data_tool()` missing `self`<br>❌ `PDFLoader` not imported | ✅ Added `self` to methods<br>✅ Imported `PDFLoader` from `langchain.document_loaders` |
| `task.py` | ❌ Improper tool usage<br>❌ Wrong agent assigned to a task | ✅ Wrapped tools as methods of class instances<br>✅ Reassigned task to correct agent |
| `agents.py` | ❌ `llm` undefined<br>❌ `tool` typo instead of `tools` | ✅ Initialized LLM using `ChatGoogleGenerativeAI`<br>✅ Used correct `tools` key |
| `.env` | ❌ `GOOGLE_API_KEY` not loading | ✅ Added `load_dotenv()` and `.env` usage |
| `requirements.txt` | ❌ Build errors (`chroma-hnswlib`, `protobuf`) | ✅ Used `pipreqs` to auto-generate real dependencies<br>✅ Froze environment to `newreq.txt`<br>✅ Installed [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) |

---

## ⚙️ Setup Instructions

### 📋 Prerequisites

- Python 3.9 – 3.11
- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- `.env` file with your Gemini API key:


### 🚀 Install & Run

bash
# 1. Clone the repo
git clone https://github.com/yourusername/blood-test-analyser-debug.git
cd blood-test-analyser-debug

# 2. Setup environment
python -m venv venv
.\venv\Scripts\activate  # (or source venv/bin/activate on Unix)

# 3. Install clean dependencies
pip install -r newreq.txt

# 4. Launch app
uvicorn main:app --reload

  API Documentation
  {
  GOOGLE_API_KEY=your-gemini-api-key
  }
