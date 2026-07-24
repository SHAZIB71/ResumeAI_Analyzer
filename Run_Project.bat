@echo off

cd /d "C:\Users\Shazib\OneDrive\Desktop\ResumeAI_Analyzer"

call venv\Scripts\activate.bat

python -m streamlit run app.py

pause