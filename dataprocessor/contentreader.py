
def read_txt_file(file_path,encoding='utf8'):
    with open(file_path, encoding=encoding) as f:
        for line in f:
            yield line.strip()
