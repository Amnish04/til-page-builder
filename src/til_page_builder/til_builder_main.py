"""Entry point of the application"""

import os
import sys
import pathlib
import shutil
import version
from builder.html_builder import HtmlBuilder
from utils.helper_functions import has_txt_extension, has_md_extension
from utils.commandline import CommandlineParser
from models.html_file import HtmlFile


class App:
    def __init__(self):
        self.cl_args = CommandlineParser().get_args()
        self.html_builder = HtmlBuilder()

    def run(self, input_path=None, test_context=False):
        """Entry point for the app"""

        # Check for exit commands (Return if any branch is entered)
        if self.cl_args.version:
            print(f"{version.__app_name__}: {version.__version__}")
            if not test_context:
                sys.exit(0)

        # Execute parse functions
        input_path = self.cl_args.input_path if input_path is None else input_path

        if input_path is None:
            print(
                "You need to specify a file or folder of text files that need to be converted!"
            )
            sys.exit(-1)

        # Check if the pathname is a directory
        if os.path.isdir(input_path):
            # Create a Path object for the directory
            directory = pathlib.Path(input_path)

            # Use the rglob() method to get a list of all files in the directory and its subdirectories
            files_in_directory = list(
                filter(
                    lambda file_path: os.path.isfile(file_path)
                    and has_txt_extension(file_path)
                    or has_md_extension(file_path),
                    list(
                        map(
                            lambda file_path: str(file_path.absolute()).replace(
                                "\\", "/"
                            ),
                            list(directory.rglob("*")),
                        )
                    ),
                )
            )

            files_to_be_generated = []

            for file in files_in_directory:
                files_to_be_generated.append(
                    self.html_builder.generate_html_file_object(file)
                )

            HtmlFile.generate_files(files_to_be_generated)

            # Copy theme/styles into the generated bundle
            shutil.copytree("./themes", f"{self.cl_args.output}/themes")
            shutil.copytree("./assets", f"{self.cl_args.output}/assets")

        elif os.path.isfile(input_path):
            # Check if a text file is supplied
            if has_txt_extension(input_path) or has_md_extension(input_path):
                HtmlFile.generate_files(
                    [self.html_builder.generate_html_file_object(input_path)]
                )
            else:
                print(
                    f"Only text and markdown files are supported. {input_path} is not a text or markdown file!"
                )
                sys.exit(-1)
        else:
            print(
                f"'{input_path}' does not exist or is neither a file nor a directory."
            )
            sys.exit(-1)

        # Everything went well
        if not test_context:
            sys.exit(0)


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
