import os
import PyPDF2
from config import settings as st


def get_pdf_files(path_folder: str = st.path_data) -> list: 
    files_pdf = []

    for file in os.listdir(path_folder):
        path_file = os.path.join(path_folder, file)
        
        if file.endswith('.pdf') and os.stat(path_file).st_size < 100000:
            files_pdf.append(path_file)

    return files_pdf


def main():
    files_pdf = get_pdf_files()

    pdfMerge = PyPDF2.PdfMerger(strict=False)

    for filename in files_pdf:
        with open(filename, 'rb') as pdfFile:
            pdfReader = PyPDF2.PdfReader(pdfFile)
            pdfMerge.append(pdfReader)

    
    pdfMerge.write(os.path.join(st.path_result_files, 'result.pdf'))


if __name__ == '__main__':
    main()
