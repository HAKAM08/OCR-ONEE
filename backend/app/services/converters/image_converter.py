import os


class ImageConverter:
    """
    Handles image documents.

    Images do not require conversion.
    """

    SUPPORTED_EXTENSIONS = {
        ".jpg",
        ".jpeg",
        ".png"
    }

    @staticmethod
    def convert(file_path: str) -> list[str]:

        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        return [file_path]