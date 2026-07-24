def resume_grade(score):
    if score >= 90:
        return "A+", "Outstanding"

    elif score >= 80:
        return "A", "Excellent"

    elif score >= 70:
        return "B", "Strong"

    elif score >= 60:
        return "C", "Needs Improvement"

    elif score >= 50:
        return "D", "Weak"

    else:
        return "F", "Poor"


def grade_description(score):
    grade, status = resume_grade(score)
    if score >= 90:
        return (
            grade,
            status,
            "Your resume is highly ATS-friendly and competitive."
        )
    elif score >= 80:
        return (
            grade,
            status,
            "Your resume is strong and likely to pass ATS screening well."
        )
    elif score >= 70:
        return (
            grade,
            status,
            "Your resume is solid, but a few improvements can "
            "boost visibility."
        )
    elif score >= 60:
        return (
            grade,
            status,
            "Your resume needs more keyword alignment and formatting clarity."
        )
    elif score >= 50:
        return (
            grade,
            status,
            "Your resume needs significant improvement to meet "
            "ATS expectations."
        )
    return (
        grade,
        status,
        "Your resume is far below the expected ATS benchmark."
    )
