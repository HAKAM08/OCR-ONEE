from lingua import Language
from lingua import LanguageDetectorBuilder


class LanguageDetectionService:
    """
    Service responsible for detecting the
    language of OCR extracted text.
    """

    detector = LanguageDetectorBuilder.from_languages(

        Language.ENGLISH,
        Language.FRENCH,
        Language.ARABIC

    ).build()

    LANGUAGE_CODES = {

        Language.ENGLISH: "eng",

        Language.FRENCH: "fra",

        Language.ARABIC: "ara"

    }

    @classmethod
    def detect(cls, text: str) -> str:

        if not text or len(text.strip()) < 10:
            return "unknown"

        language = cls.detector.detect_language_of(text)

        if language is None:
            return "unknown"

        return cls.LANGUAGE_CODES.get(
            language,
            "unknown"
        )