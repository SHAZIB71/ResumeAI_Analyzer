from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError


def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        pages = []

        for page in reader.pages:
            page_text = page.extract_text() or ""
            pages.append(page_text)

        text = "\n".join(pages).strip()

        if not text:
            raise ValueError(
                "The uploaded PDF does not contain readable text."
            )

        return text

    except (PdfReadError, ValueError) as exc:
        raise ValueError(f"Unable to read the PDF. {exc}") from exc
