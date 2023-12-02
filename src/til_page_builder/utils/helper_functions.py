import os


def has_txt_extension(file_path):
    # pylint: disable=unused-variable
    file_name, file_extension = os.path.splitext(file_path)
    # pylint: enable=unused-variable

    return file_extension.lower() == ".txt"


def has_md_extension(file_path):
    # pylint: disable=unused-variable
    file_name, file_extension = os.path.splitext(file_path)
    # pylint: enable=unused-variable

    return file_extension.lower() == ".md"


def has_extension(file_path, extension):
    # pylint: disable=unused-variable
    file_name, file_extension = os.path.splitext(file_path)
    # pylint: enable=unused-variable

    return file_extension.lower() == extension
