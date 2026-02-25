from typing import Iterable

import fitz


def parse_pages(text: str, page_count: int) -> list[int]:
    pages = set()

    for part in text.split(","):
        part = part.strip()
        if "-" in part:
            try:
                a, b = map(int, part.split("-"))
                if a > b:
                    a, b = b, a
                pages.update(range(a - 1, b))
            except ValueError:
                continue
        elif part.isdigit():
            pages.add(int(part) - 1)

    return sorted(p for p in pages if 0 <= p < page_count)


def merge_pdfs(items: Iterable[tuple[str, str, str]], output_path: str) -> None:
    """
    items:
        Iterable (pdf_path, mode, custom_text)
        mode: 'all' | 'custom'
    """

    out = fitz.open()

    for path, mode, custom_text in items:
        doc = fitz.open(path)

        if mode == "all":
            out.insert_pdf(doc)

        else:
            pages = parse_pages(custom_text, doc.page_count)
            for p in pages:
                out.insert_pdf(doc, from_page=p, to_page=p)

        doc.close()

    out.save(output_path)
    out.close()


def rotate_pdfs(doc: fitz.Document, angle: int, pages_to_rotate: list[int]):
    """Modifies the fitz document object in place."""
    for p_index in pages_to_rotate:
        if 0 <= p_index < doc.page_count:
            page = doc[p_index]
            new_rot = (page.rotation + angle) % 360
            page.set_rotation(new_rot)
    return doc
