import os

INPUT_DIR = os.path.abspath(os.path.dirname(__file__) + '/../inputs')


def open_input(filename):
    full_path = os.path.join(INPUT_DIR, filename)
    return open(full_path)
