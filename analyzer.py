import json

from google import genai

from config import GEMINI_API_KEY, MODEL_NAME, API_CONFIGURED
from prompts import ATS_PROMPT


class ResumeAnalyzer:

    def __init__(self):
        self.client = None
        if API_CONFIGURED and GEMINI_API_KEY:
            self.client = genai.Client(api_key=GEMINI_API_KEY)

    def analyze(self, resume_text, job_description=""):

        if not self.client:
            return {
                "ats_score": 0,
                "job_match": 0,
                "summary": (
                    "AI analysis is unavailable because the Gemini API key "
                    "is not configured. Please set GEMINI_API_KEY in your "
                    "environment or .env file."
                ),
                "skills": [],
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "suggestions": []
            }

        prompt = ATS_PROMPT.replace(
            "__RESUME__", resume_text or ""
        ).replace(
            "__JOB_DESCRIPTION__", job_description or ""
        )

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            text = response.text.strip()

            if text.startswith("```json"):
                text = text.replace("```json", "")

            text = text.replace("```", "").strip()

            return json.loads(text)

        except Exception as e:

            print(e)

            return {
                "ats_score": 0,
                "job_match": 0,
                "summary": f"AI Error: {e}",
                "skills": [],
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "suggestions": []
            }
