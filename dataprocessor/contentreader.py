import pandas as pd


def read_txt_file(file_path: str, encoding='utf8'):
    with open(file_path, encoding=encoding) as f:
        for line in f:
            yield line.strip()


def read_csv_file(file_path, sep=",", delimiter=None, header=0):
    return pd.read_csv(file_path, sep=sep, delimiter=delimiter, header=header)
