# ResumeAI Analyzer

ResumeAI Analyzer is an AI-powered resume analysis app built with Python, Streamlit, and Google Gemini. It helps users evaluate resumes for ATS compatibility, generate a summary, detect key skills, and create a professional cover letter.

## Features

- ATS Resume Score
- Job Match Score
- Resume Summary
- Skills Detection
- Missing Skills
- AI Suggestions
- Cover Letter Generator
- Resume PDF Report
- Resume History (SQLite)

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- ReportLab
- Plotly
- PyPDF2

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Gemini API key:
   - Copy .env.example to .env
   - Add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   MODEL_NAME=gemini-flash-latest
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure

- app.py - Main Streamlit application
- analyzer.py - Resume analysis using Gemini
- cover_letter.py - Cover letter generation
- database.py - Resume history storage
- report_generator.py - PDF generation
- pdf_reader.py - PDF text extraction
- utils/grading.py - Resume grade logic

## Notes

If the Gemini API key is not configured, the app will still open but AI features will be disabled until the key is provided.

## Desktop App Build

To build a Windows executable:

```bash
pip install pyinstaller
python build_exe.py
```

The executable will be generated in the dist folder.