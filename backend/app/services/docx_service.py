from docx import Document


class DOCXService:

    @staticmethod
    def extract_text(file_path: str) -> str:

        doc = Document(file_path)

        paragraphs = []

        for paragraph in doc.paragraphs:

            if paragraph.text.strip():

                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)