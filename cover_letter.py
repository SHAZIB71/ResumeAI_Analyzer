from google import genai

from config import GEMINI_API_KEY, MODEL_NAME, API_CONFIGURED


class CoverLetterGenerator:

    def __init__(self):
        self.client = None
        if API_CONFIGURED and GEMINI_API_KEY:
            self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, resume_text, job_description):

        if not self.client:
            return (
                "Cover letter generation is unavailable because the Gemini "
                "API key is not configured. Please set GEMINI_API_KEY in "
                "your environment or .env file."
            )

        prompt = f"""
You are a professional HR Recruiter and Career Coach.

Your task is to generate a professional ATS-friendly Cover Letter.

Resume:
{resume_text}

Job Description:
{job_description}

Instructions:

1. Write a professional cover letter.
2. Use a formal and confident tone.
3. Mention the candidate's relevant skills and experience.
4. Match the resume with the job description.
5. Keep it between 300–400 words.
6. End with a professional closing.
7. Do NOT use placeholders like [Your Name].
8. Return only the cover letter text.

Cover Letter:
"""

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            return f"""
Unable to generate Cover Letter.

Reason:
{str(e)}

Please try again after a few minutes.
"""
