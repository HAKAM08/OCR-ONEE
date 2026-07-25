import time

import pytesseract

from app.core.config import settings
from app.core.ocr.ocr_processing_result import OCRProcessingResult
from app.services.image_processing_service import ImageProcessingService
from app.services.text_cleaning_service import TextCleaningService
from app.services.language_detection_service import LanguageDetectionService
from app.services.ocr_correction_service import OCRCorrectionService
from app.services.ocr_correction_service import OCRCorrectionService
# Configure Tesseract executable
pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD
from app.services.image_processing_service import ImageProcessingService
from app.services.text_cleaning_service import TextCleaningService
from app.services.language_detection_service import LanguageDetectionService
from app.services.ocr_correction_service import OCRCorrectionService

class OCRService:
    """
    OCR engine responsible for extracting text
    from one or multiple images.
    """

    @staticmethod
    def extract_text(image) -> str:
        return pytesseract.image_to_string(
            image,
            lang=settings.OCR_LANGUAGE
        )

    @staticmethod
    def extract_data(image) -> dict:
        return pytesseract.image_to_data(
            image,
            lang=settings.OCR_LANGUAGE,
            output_type=pytesseract.Output.DICT
        )

    @staticmethod
    def calculate_average_confidence(data: dict) -> float:

        confidences = []

        for value in data["conf"]:

            try:

                score = float(value)

                if score >= 0:
                    confidences.append(score)

            except ValueError:
                continue

        if not confidences:
            return 0.0

        return round(
            sum(confidences) / len(confidences),
            2
        )

    @classmethod
    def process_image(
        cls,
        image_path: str
    ) -> tuple[str, float]:
        """
        Processes a single image.
        Returns:
            text,
            confidence
        """

        processed_image = ImageProcessingService.preprocess(
            image_path
        )

        raw_text = cls.extract_text(
            processed_image
        )

        cleaned_text = TextCleaningService.clean(
            raw_text
        )

        corrected_text = OCRCorrectionService.correct(
            cleaned_text
        )
        corrected_text = OCRCorrectionService.correct(
            cleaned_text
)

        data = cls.extract_data(
            processed_image
        )

        confidence = cls.calculate_average_confidence(
            data
        )

        return (
            corrected_text,
            confidence
        )

    @classmethod
    def process_images(
        cls,
        images: list[str]
    ) -> OCRProcessingResult:
        """
        Processes multiple images and
        returns a single OCR result.
        """

        start_time = time.perf_counter()

        pages_text = []

        confidences = []

        for image_path in images:

            text, confidence = cls.process_image(
                image_path
            )

            pages_text.append(text)

            confidences.append(confidence)

        final_text = "\n\n".join(
            pages_text
        )
        language = LanguageDetectionService.detect(
            final_text
)
        average_confidence = 0.0

        if confidences:

            average_confidence = round(
                sum(confidences) / len(confidences),
                2
            )

        processing_time = round(
            time.perf_counter() - start_time,
            2
        )

        return OCRProcessingResult(

            text=final_text,

            confidence=average_confidence,

            processing_time=processing_time,

            page_count=len(images),

            language=language

)