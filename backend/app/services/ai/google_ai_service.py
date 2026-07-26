from google import genai
from app.core.config import settings


class GoogleAIService:
    """
    Google Gemini service used for OCR correction.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    def correct_ocr(self, text: str) -> str:

        prompt = f"""
You are an OCR correction engine.

Your task is ONLY to correct OCR mistakes.

Rules:

- Never invent information.
- Never summarize.
- Never answer questions.
- Preserve names.
- Preserve numbers.
- Preserve dates.
- Preserve formatting.
- Correct only obvious OCR errors.
- Return ONLY the corrected text.

OCR Text:

{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )

        if not response.text:
            return text

        return response.text.strip()