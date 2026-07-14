import os

import fitz


class PDFConverter:
    """
    Converts every page of a PDF
    into PNG images.
    """

    OUTPUT_DPI = 300

    @classmethod
    def convert(
        cls,
        pdf_path: str
    ) -> list[str]:

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(pdf_path)

        output_folder = os.path.splitext(pdf_path)[0]

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        pdf = fitz.open(pdf_path)

        pages = []

        zoom = cls.OUTPUT_DPI / 72

        matrix = fitz.Matrix(
            zoom,
            zoom
        )

        for page_number in range(len(pdf)):

            page = pdf.load_page(page_number)

            pix = page.get_pixmap(
                matrix=matrix
            )

            image_path = os.path.join(
                output_folder,
                f"page_{page_number + 1}.png"
            )

            pix.save(image_path)

            pages.append(image_path)

        pdf.close()

        return pages