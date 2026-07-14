import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    # ===========================
    # Database
    # ===========================

    DATABASE_URL = os.getenv("DATABASE_URL")

    # ===========================
    # Security
    # ===========================

    SECRET_KEY = os.getenv("SECRET_KEY")

    ALGORITHM = os.getenv("ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
    )

    # ===========================
    # Storage
    # ===========================

    UPLOAD_DIRECTORY = os.getenv(
        "UPLOAD_DIRECTORY",
        "app/uploads/documents"
    )

    MAX_FILE_SIZE = int(
        os.getenv(
            "MAX_FILE_SIZE",
            20971520
        )
    )

    # ===========================
    # OCR
    # ===========================

    TESSERACT_CMD = os.getenv(
        "TESSERACT_CMD"
    )

    OCR_LANGUAGE = os.getenv(
        "OCR_LANGUAGE",
        "fra+eng"
    )

    # ===========================
    # Elasticsearch
    # ===========================

    ELASTICSEARCH_URL = os.getenv(
        "ELASTICSEARCH_URL"
    )

    ELASTICSEARCH_INDEX = os.getenv(
        "ELASTICSEARCH_INDEX",
        "documents"
    )


settings = Settings()