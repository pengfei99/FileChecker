from dataprocessor.contentreader import read_txt_file


def test_read_txt_file():
    file_path = "/home/pliu/git/FileChecker/data/test.txt"
    lines = read_txt_file(file_path)
    for line in lines:
        print(line)
