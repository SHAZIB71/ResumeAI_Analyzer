def resume_grade(score):

    if score >= 90:
        return "A+", "Outstanding"

    elif score >= 80:
        return "A", "Excellent"

    elif score >= 70:
        return "B", "Good"

    elif score >= 60:
        return "C", "Average"

    elif score >= 50:
        return "D", "Needs Improvement"

    else:
        return "F", "Poor"
