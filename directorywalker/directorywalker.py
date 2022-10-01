import os


def list_files(dir_path):
    r = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            r.append(os.path.join(root, name))
    return r


