from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors

output = 'sample_resume.pdf'
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='ResumeTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#1e3a8a')))
styles.add(ParagraphStyle(name='ResumeSubtitle', parent=styles['BodyText'], fontName='Helvetica', fontSize=10, leading=12, textColor=colors.HexColor('#475569')))
styles.add(ParagraphStyle(name='SectionTitle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=colors.HexColor('#2563eb'), spaceAfter=6))
styles.add(ParagraphStyle(name='Body', parent=styles['BodyText'], fontName='Helvetica', fontSize=10, leading=12, spaceAfter=4))
if 'Bullet' not in styles:
    styles.add(ParagraphStyle(name='Bullet', parent=styles['BodyText'], fontName='Helvetica', fontSize=10, leading=12, leftIndent=14, spaceAfter=3))

story = []
story.append(Paragraph('Shazib Huda', styles['ResumeTitle']))
story.append(Paragraph('Python Developer | AI Enthusiast | Problem Solver', styles['ResumeSubtitle']))
story.append(Paragraph('shazib@example.com | +92 300 1234567 | LinkedIn: linkedin.com/in/shazib', styles['ResumeSubtitle']))
story.append(Spacer(1, 12))

story.append(Paragraph('Professional Summary', styles['SectionTitle']))
story.append(Paragraph('Motivated software developer with experience building AI-powered applications, automation tools, and user-friendly web apps. Strong knowledge of Python, Streamlit, SQL, and modern AI integrations. Passionate about creating practical solutions that improve productivity and decision-making.', styles['Body']))
story.append(Spacer(1, 8))

story.append(Paragraph('Skills', styles['SectionTitle']))
skills = ['Python', 'Streamlit', 'SQL', 'SQLite', 'Git/GitHub', 'Google Gemini API', 'PyPDF2', 'ReportLab', 'Plotly', 'Problem Solving']
story.append(Paragraph(', '.join(skills), styles['Body']))
story.append(Spacer(1, 8))

story.append(Paragraph('Experience', styles['SectionTitle']))
story.append(Paragraph('AI Resume Analyzer Project', styles['Body']))
story.append(Paragraph('Developed an AI-powered resume analysis application with features like ATS scoring, skill detection, cover letter generation, PDF reporting, and history tracking using Python and Streamlit.', styles['Bullet']))
story.append(Paragraph('Integrated Gemini AI for resume evaluation and automated content generation.', styles['Bullet']))
story.append(Paragraph('Built a polished web interface and improved user experience with modern styling and clear result reporting.', styles['Bullet']))
story.append(Spacer(1, 8))

story.append(Paragraph('Education', styles['SectionTitle']))
story.append(Paragraph('Bachelor of Science in Computer Science', styles['Body']))
story.append(Paragraph('University Name | 2021 - 2025', styles['Body']))
story.append(Spacer(1, 8))

story.append(Paragraph('Projects', styles['SectionTitle']))
story.append(Paragraph('ResumeAI Analyzer', styles['Body']))
story.append(Paragraph('Created a full-stack-style AI app for resume analysis and career support with PDF processing, analytics, and report generation.', styles['Bullet']))
story.append(Paragraph('Automated cover letter creation based on resume and job description inputs.', styles['Bullet']))

pdf = SimpleDocTemplate(output, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
pdf.build(story)
print(output)
