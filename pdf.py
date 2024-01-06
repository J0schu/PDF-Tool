from PyPDF2 import PdfMerger

def merger(pdfs, output_name):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(output_name)
    merger.close()
