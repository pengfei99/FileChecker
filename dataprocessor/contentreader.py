import pandas as pd
from PyPDF2 import PdfReader


def read_txt_file(file_path: str, encoding='utf8'):
    with open(file_path, encoding=encoding) as f:
        for line in f:
            yield line.strip()


def read_csv_file(file_path, sep=",", delimiter=None, header=0):
    return pd.read_csv(file_path, sep=sep, delimiter=delimiter, header=header)


def read_pdf_file(file_path: str):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    for i in range(0, number_of_pages):
        page = reader.pages[i]
        yield i, page.extract_text()


def read_excel_file(file_path: str, index_col=None, header=None, sheet_name=None):
    return pd.read_excel(file_path, index_col=index_col, header=header, sheet_name=sheet_name)
