from datetime import datetime
from pypdf import PdfMerger, PdfReader, PdfWriter
import os
import pwd

time = datetime.utcnow().strftime(f"D\072%Y%m%d%H%M%S")

def merger(pdfs, output_name):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.add_metadata(
        {
        "/Author": pwd.getpwuid(os.getuid())[4], # only for Linux
        "/Producer": "PDF-Tool",
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
