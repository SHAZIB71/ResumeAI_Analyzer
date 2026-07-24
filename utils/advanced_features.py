import re
import zipfile
from xml.sax.saxutils import escape


STOP_WORDS = {
    "the", "and", "for", "with", "your", "this", "that", "have", "from",
    "into", "will", "were", "been", "are", "can", "could", "should", "would",
    "developer", "engineer", "software", "team", "role", "job", "resume"
}


def _extract_keywords(text, limit=8):
    words = re.findall(r"[a-zA-Z+#.]+", text.lower())
    filtered = []
    for word in words:
        clean = re.sub(r"[^a-z]", "", word)
        if len(clean) >= 3 and clean not in STOP_WORDS:
            filtered.append(clean)
    return list(dict.fromkeys(filtered))[:limit]


def build_resume_rewriter(resume_text, job_description=""):
    keywords = _extract_keywords(job_description or resume_text, limit=6)
    summary = (
        "Results-driven professional with strong experience in building "
        "practical software solutions, improving user experience, and "
        "delivering value through automation and modern technology."
    )
    if keywords:
        summary += (
            f" Skills and experience are aligned with "
            f"{', '.join(keywords)}."
        )

    bullets = [
        "Developed and delivered reliable software solutions with "
        "measurable impact.",
        "Applied strong problem-solving, communication, and technical "
        "execution skills.",
        "Focused on quality, usability, and continuous improvement."
    ]

    if keywords:
        bullets.append(
            f"Strengthened alignment with key requirements such as "
            f"{', '.join(keywords[:4])}."
        )

    return {
        "summary": summary,
        "bullets": bullets,
        "title": "Enhanced Resume Summary"
    }


def build_interview_prep(resume_text, job_description=""):
    keywords = _extract_keywords(job_description or resume_text, limit=6)
    questions = [
        "Tell me about your most relevant project and the impact it created.",
        "How do you approach solving unfamiliar technical problems?",
        "Which tools or technologies do you use most effectively in your "
        "work?",
        "How would you explain your experience to a hiring manager in one "
        "minute?"
    ]
    if keywords:
        questions.append(
            f"How would you tailor your experience to a role focused on "
            f"{', '.join(keywords[:3])}?"
        )

    return {
        "title": "Interview Preparation",
        "questions": questions,
        "tips": [
            "Practice clear examples using the STAR method.",
            "Prepare 2–3 strong project stories in advance.",
            "Review the job description carefully and align your answers "
            "with it."
        ]
    }


def build_linkedin_optimizer(resume_text, job_description=""):
    keywords = _extract_keywords(job_description or resume_text, limit=6)
    headline = "Software Developer | AI Enthusiast | Problem Solver"
    if keywords:
        headline = f"Software Developer | {' | '.join(keywords[:4])}"

    about = (
        "I build practical software solutions and enjoy creating products "
        "that solve real-world problems. My work focuses on clean "
        "implementation, strong problem-solving, and user-friendly "
        "experiences."
    )

    return {
        "title": "LinkedIn Optimizer",
        "headline": headline,
        "about": about
    }


def build_email_generator(
    job_title="Software Developer",
    company_name="Company"
):
    subject = f"Application for {job_title} Role"
    body = (
        f"Dear Hiring Team,\n\n"
        f"I am very interested in the {job_title} position at {company_name}. "
        "My background and experience align well with the role, and I would "
        "welcome the opportunity to discuss how I can contribute to your "
        "team.\n\n"
        "Thank you for your time and consideration.\n\n"
        "Best regards,\n"
        "[Your Name]"
    )

    return {
        "title": "Email Generator",
        "subject": subject,
        "body": body
    }


def export_text_to_docx(text, filename):
    paragraphs = [p.strip() for p in text.splitlines() if p.strip()]
    body_parts = []
    for paragraph in paragraphs:
        body_parts.append(
            "<w:p><w:r><w:t>{}</w:t></w:r></w:p>".format(escape(paragraph))
        )

    document_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/"
    "wordprocessingml/2006/main">
  <w:body>
    {body}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>
    </w:sectPr>
  </w:body>
</w:document>""".format(body="".join(body_parts))

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels"
    ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/"
    "relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
    Target="word/document.xml"/>
</Relationships>"""

    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", rels)
        docx.writestr("word/document.xml", document_xml)

    return filename
