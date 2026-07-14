from app.services.converters.image_converter import ImageConverter
from app.services.converters.pdf_converter import PDFConverter


class ConverterFactory:
    """
    Returns the appropriate converter
    according to the document type.
    """

    @staticmethod
    def get_converter(extension: str):

        extension = extension.lower()

        if extension in {
            ".jpg",
            ".jpeg",
            ".png"
        }:
            return ImageConverter

        if extension == ".pdf":
            return PDFConverter

        raise ValueError(
            f"Unsupported document type: {extension}"
        )