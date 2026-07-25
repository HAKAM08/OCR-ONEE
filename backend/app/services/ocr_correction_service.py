import requests


class OCRCorrectionService:
    """
    Uses a local Llama 3.2 model through Ollama
    to improve OCR text.
    """

    URL = "http://localhost:11434/api/generate"
    MODEL = "llama3.2:1b"

    @classmethod
    def correct(cls, text: str) -> str:

        if not text.strip():
            return text

        prompt = f"""
You are an OCR correction engine.

Your only task is to correct OCR errors in a document.

Rules:

- Return ONLY the corrected document.
- Do NOT explain your changes.
- Do NOT include notes, comments or examples.
- Do NOT repeat these instructions.
- Do NOT add introductions or conclusions.
- Do NOT invent missing sentences.
- Do NOT summarize.
- Preserve the original language.
- Preserve names, dates, numbers and proper nouns.
- Preserve paragraph order.
- Fix OCR spelling mistakes.
- Restore missing spaces between merged words.
- Restore missing apostrophes when obvious.
- Fix broken words split incorrectly across lines.
- Correct obvious accent errors.
- If you are not confident, keep the original word.



Now correct the following OCR text.

{text}
"""

        try:
            response = requests.post(
                cls.URL,
                json={
                    "model": cls.MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
    "temperature": 0,
    "top_p": 0.05,
    "top_k": 10,
    "repeat_penalty": 1.1,
    "num_predict": 4096,
}
                },
                timeout=300
            )

            response.raise_for_status()

            result = response.json()

            corrected = result.get("response", "").strip()

            print("\n" + "=" * 80)
            print("ORIGINAL OCR TEXT")
            print("=" * 80)
            print(text)

            print("\n" + "=" * 80)
            print("OLLAMA CORRECTED TEXT")
            print("=" * 80)
            print(corrected)

            print("\n" + "=" * 80)
            print("TEXT CHANGED:", text != corrected)
            print("=" * 80)

            if corrected:
                return corrected

            print("[OCRCorrectionService] Ollama returned an empty response. Using original OCR text.")
            return text

        except Exception as e:
            print(f"[OCRCorrectionService] Error: {e}")
            print("[OCRCorrectionService] Falling back to original OCR text.")
            return text