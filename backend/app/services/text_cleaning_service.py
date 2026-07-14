import re


class TextCleaningService:
    """
    Service responsable du nettoyage du texte
    extrait par le moteur OCR.
    """

    @staticmethod
    def remove_extra_spaces(text: str) -> str:
        """
        Supprime les espaces multiples.
        """
        return re.sub(r"\s+", " ", text)

    @staticmethod
    def remove_empty_lines(text: str) -> str:
        """
        Supprime les lignes vides.
        """
        lines = text.splitlines()

        cleaned_lines = [
            line.strip()
            for line in lines
            if line.strip()
        ]

        return "\n".join(cleaned_lines)

    @staticmethod
    def remove_non_printable(text: str) -> str:
        """
        Supprime les caractères non imprimables.
        """
        return "".join(
            character
            for character in text
            if character.isprintable()
        )

    @classmethod
    def clean(cls, text: str) -> str:
        """
        Pipeline complet de nettoyage.
        """

        text = cls.remove_non_printable(text)

        text = cls.remove_empty_lines(text)

        text = cls.remove_extra_spaces(text)

        return text.strip()