import os
import uuid
import shutil

from fastapi import UploadFile


class FileService:

    UPLOAD_DIR = "app/uploads/documents"

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".doc",
        ".docx",
        ".png",
        ".jpg",
        ".jpeg"
    }

    MAX_SIZE = 20 * 1024 * 1024


    @classmethod
    def save_file(cls, file: UploadFile):

        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in cls.ALLOWED_EXTENSIONS:
            raise ValueError(
                "Type de fichier non autorisé."
            )

        os.makedirs(cls.UPLOAD_DIR, exist_ok=True)

        filename = f"{uuid.uuid4()}{extension}"

        filepath = os.path.normpath(
            os.path.join(
                cls.UPLOAD_DIR,
                filename
    )
)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "original_filename": file.filename,
            "filename": filename,
            "filepath": filepath,
            "extension": extension
        }