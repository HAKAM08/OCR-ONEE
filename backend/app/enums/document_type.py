from enum import Enum


class DocumentType(str, Enum):
    COMMON = "COMMON"
    CONFIDENTIAL = "CONFIDENTIAL"