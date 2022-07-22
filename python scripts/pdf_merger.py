import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file[:-4])
    merger.write("combined_pdf")
