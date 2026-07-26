import os

from app.services.converters.converter_factory import ConverterFactory


class DocumentConversionService:
    """
    Converts any supported document
    into a list of images.
    """

    @staticmethod
    def convert(
        file_path: str
    ) -> list[str]:

        extension = os.path.splitext(
            file_path
        )[1]

        converter = ConverterFactory.get_converter(
            extension
        )

        return converter.convert(
            file_path
        )