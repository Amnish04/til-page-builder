import os
# A virtual representation of the file to be generated
class File:
    def __init__(self, file_path, file_content):
        self.file_path = file_path
        self.file_content = file_content

    # Write the file to the disk based on path and content
    def generate_html_file(self):
        write_path = self.file_path.replace(f'{os.path.splitext(self.file_path)[1]}', '.html')

        with open(write_path, "w") as file:
            file.write(self.file_content)
