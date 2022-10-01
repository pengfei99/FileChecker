from dataprocessor.directorywalker import list_files


def test_list_files():
    path_dir = "/home/pliu/git/FileChecker"
    file_list = list_files(path_dir)
    print(file_list)
