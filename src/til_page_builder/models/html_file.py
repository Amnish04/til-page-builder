import os
import shutil
from typing import List
from til_page_builder.utils.commandline import CommandlineParser


class HtmlFile:
    """A virtual representation of the html file to be generated"""

    def __init__(self, file_path, file_content):
        """
        :param file_path: Write
        :param file_content: _description_
        """

        self.file_path = file_path
        self.file_content = file_content

    # Write the file to the disk based on path and content
    def generate_html_file(self):
        """Creates a new file on the disk, or overrides existing, based on `self.file_path` and `self.file_content`"""
        write_path = self.file_path.replace(
            f"{os.path.splitext(self.file_path)[1]}", ".html"
        )

        with open(write_path, "w") as file:
            file.write(self.file_content)

    @staticmethod
    def generate_files(files_to_be_generated: List["HtmlFile"]):
        """Writes the provided HtmlFile(s) to the disk

        :param files_to_be_generated:  A list of HtmlFile objects to be written to disk
        """
        cl_args = CommandlineParser().get_args()

        # Delete the output directory if it already exists
        if os.path.isdir(cl_args.output):
            # Delete the folder structure
            shutil.rmtree(cl_args.output)

        # Generate the output directory
        os.makedirs(cl_args.output, exist_ok=True)

        # Generate an html file for each text file
        for file in files_to_be_generated:
            file.generate_html_file()
