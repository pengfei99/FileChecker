from dataprocessor.contentreader import read_txt_file, read_csv_file, read_pdf_file

root_path = "/home/pliu/git/FileChecker/data"


def test_read_txt_file():
    file_path = f"{root_path}/test.txt"
    lines = read_txt_file(file_path)
    for line in lines:
        print(line)


def test_read_csv_file_with_header():
    file_path = f"{root_path}/with_header.csv"
    df = read_csv_file(file_path)
    print(df.head())


def test_read_csv_file_without_header():
    file_path = f"{root_path}/without_header.csv"
    df = read_csv_file(file_path, header=None)
    print(df.head())


def test_read_pdf_file():
    file_path = f"{root_path}/file-sample.pdf"
    page_nums, texts = zip(*read_pdf_file(file_path))
    for i in range(0,len(page_nums)):
        print(f"At page {page_nums[i]}:")
        print(f"content: {texts[i]}")



