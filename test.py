from pdf_reader import extract_text_from_pdf
from analyzer import ResumeAnalyzer

# Read Resume
file = "Shazib_Huda_Resume.pdf"
resume_text = extract_text_from_pdf(file)

# Analyze Resume
analyzer = ResumeAnalyzer()
result = analyzer.analyze(resume_text)

print(result)