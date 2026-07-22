import json
from google import genai
from config import GEMINI_API_KEY, MODEL_NAME


class ResumeAnalyzer:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def analyze(self, resume_text, job_description=""):

        prompt = f"""
You are an ATS Resume Expert.

Analyze the following resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON.

Example:

{{
    "ats_score": 85,
    "job_match": 80,
    "summary": "Short professional summary.",
    "skills": [
        "Python",
        "Java"
    ],
    "strengths": [
        "Strong Projects"
    ],
    "weaknesses": [
        "Needs SQL"
    ],
    "missing_skills": [
        "SQL",
        "React"
    ],
    "suggestions": [
        "Add SQL projects",
        "Improve ATS keywords"
    ]
}}

Do not write anything except JSON.
"""

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            text = response.text.strip()

            # Remove markdown if Gemini returns ```json
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return json.loads(text)

        except Exception as e:

            return {
                "ats_score": 0,
                "job_match": 0,
                "summary": f"AI Service Error:\n\n{str(e)}",
                "skills": [],
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "suggestions": []
            }