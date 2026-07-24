ATS_PROMPT = """
You are an expert ATS Resume Analyzer and HR-tech evaluator.

Analyze the provided resume against the given job description.
Focus on ATS friendliness, relevance, clarity, keyword alignment,
and hiring potential.

Resume:
__RESUME__

Job Description:
__JOB_DESCRIPTION__

Return ONLY valid JSON with this exact structure:
{
    "ats_score": 90,
    "job_match": 85,
    "summary": "Short professional summary",
    "skills": [
        "Python",
        "SQL"
    ],
    "strengths": [
        "Strong Python knowledge"
    ],
    "weaknesses": [
        "No SQL projects"
    ],
    "missing_skills": [
        "Docker",
        "AWS"
    ],
    "suggestions": [
        "Build SQL projects",
        "Learn Docker"
    ]
}

Important rules:
- Return only valid JSON.
- Use integers for ats_score and job_match between 0 and 100.
- Keep the summary concise but meaningful.
- Include only relevant skills and actionable suggestions.
- Do not include markdown formatting, comments, or extra text.
"""
