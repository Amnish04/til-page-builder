import os

def has_txt_extension(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.txt'

def has_txt_extension(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.txt'