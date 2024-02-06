from datetime import datetime
from pypdf import PdfMerger, PdfReader, PdfWriter

time = datetime.utcnow().strftime(f"D\072%Y%m%d%H%M%S")

def merger(pdfs, output_name, author, title, subject, keywords):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.add_metadata(
        {
        "/Author": author,
        "/Producer": "PDF-Tool",
        "/Title": title,
        "/Subject": subject,
        "/Keywords": keywords,
        "/CreationDate" : time,
        "/ModTime": time,
        }
    )
    merger.write(output_name)
    merger.close()

def get_author(filename):
    reader = PdfReader(filename)
    meta = reader.metadata
    return meta.author

def get_creator(filename):
    reader = PdfReader(filename)
    meta = reader.metadata
    return meta.creator

def get_subject(filename):
    reader = PdfReader(filename)
    meta = reader.metadata
    return meta.subject

def get_title(filename):
    reader = PdfReader(filename)
    meta = reader.metadata
    return meta.title

def add_keywords(filename, keywords):
    writer = PdfWriter()
    writer.add_metadata(
        {
        "/Keywords": keywords,
        }
    )
    with open(filename, "wb") as f:
        writer.write(f)

def add_metadata(filename, author, creator, subject, title):
    reader = PdfReader(filename)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(
        {
        "/Author": author,
        "/Producer": "PDF-Tool",
        "/Creator": creator,
        "/Subject": subject,
        "/Title": title,
        "/ModDate": time,
        }
    )
    with open(filename, "wb") as f:
        writer.write(f)