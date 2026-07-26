from enum import Enum


class DocumentStatus(str, Enum):
    """
    Possible states of a document
    during its lifecycle.
    """

    UPLOADED = "UPLOADED"

    PROCESSING = "PROCESSING"

    OCR_COMPLETED = "OCR_COMPLETED"

    INDEXED = "INDEXED"

    FAILED = "FAILED"