from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


# ---------------- Resume Report ---------------- #

def generate_pdf(result, filename="Resume_Analysis_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "ResumeAI Analyzer Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"ATS Score: {result['ats_score']}/100",
            styles["Heading2"]
        )
    )

    if "job_match" in result:

        content.append(
            Paragraph(
                f"Job Match: {result['job_match']}%",
                styles["Heading2"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Resume Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["summary"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Skills",
            styles["Heading2"]
        )
    )

    for skill in result["skills"]:
        content.append(
            Paragraph(
                "• " + skill,
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Strengths",
            styles["Heading2"]
        )
    )

    for item in result["strengths"]:
        content.append(
            Paragraph(
                "• " + item,
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Weaknesses",
            styles["Heading2"]
        )
    )

    for item in result["weaknesses"]:
        content.append(
            Paragraph(
                "• " + item,
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Suggestions",
            styles["Heading2"]
        )
    )

    for item in result["suggestions"]:
        content.append(
            Paragraph(
                "• " + item,
                styles["BodyText"]
            )
        )

    doc.build(content)

    return filename


# ---------------- Cover Letter PDF ---------------- #

def generate_cover_letter_pdf(
    cover_letter,
    filename="Cover_Letter.pdf"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Professional Cover Letter",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    paragraphs = cover_letter.split("\n")

    for para in paragraphs:

        if para.strip():

            content.append(
                Paragraph(
                    para,
                    styles["BodyText"]
                )
            )

            content.append(Spacer(1, 8))

    doc.build(content)

    return filename
