import os
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter


TARGET_FOLDER = 'pdfs-to-merge'
OUTPUT_FILENAME = 'merged.pdf'

merger = PdfMerger()
inputs = [os.path.join(TARGET_FOLDER, filename) \
          for filename in os.listdir(TARGET_FOLDER)]
try:
    for f in inputs:
        merger.append(f)
    merger.write(OUTPUT_FILENAME)
    
except:
    pdf_writer = PdfFileWriter()
    for file in inputs:
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(OUTPUT_FILENAME, 'wb') as f:
        pdf_writer.write(f)
