def create_report(result):

    report = ""

    report += "==============================\n"
    report += "     AI Resume Analysis Report\n"
    report += "==============================\n\n"

    report += f"ATS Score : {result.get('ats_score', 0)}/100\n"
    report += f"Job Match : {result.get('job_match', 0)}%\n\n"

    # Summary
    report += "Resume Summary\n"
    report += "------------------------------\n"
    report += result.get("summary", "No Summary") + "\n\n"

    # Skills
    report += "Skills\n"
    report += "------------------------------\n"

    for skill in result.get("skills", []):
        report += f"• {skill}\n"

    report += "\n"

    # Missing Skills
    report += "Missing Skills\n"
    report += "------------------------------\n"

    for skill in result.get("missing_skills", []):
        report += f"• {skill}\n"

    report += "\n"

    # Strengths
    report += "Strengths\n"
    report += "------------------------------\n"

    for item in result.get("strengths", []):
        report += f"• {item}\n"

    report += "\n"

    # Weaknesses
    report += "Weaknesses\n"
    report += "------------------------------\n"

    for item in result.get("weaknesses", []):
        report += f"• {item}\n"

    report += "\n"

    # Suggestions
    report += "Suggestions\n"
    report += "------------------------------\n"

    for item in result.get("suggestions", []):
        report += f"• {item}\n"

    return report