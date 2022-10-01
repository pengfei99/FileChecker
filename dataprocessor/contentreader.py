
def read_txt_file(file_path):
    with open(file_path, encoding='utf8') as f:
        for line in f:
            print(line.strip())
