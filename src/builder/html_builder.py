import os
import shutil
from yattag import Doc, indentation
from utils.commandline import cl_args
from models.file import File 

# Global variables
OUTPUT_PATH = cl_args.output # Output directory for files
FILES_TO_BE_GENERATED = []   # A list of File objects

def generate_html_for_file(file_path):
    with open(file_path, "r") as file:
        # Create the html virtual document
        doc, tag, text = Doc().tagtext()
        lines = file.readlines()
        line_cursor_position = 0

        # Check for a title
        if is_title_present(lines):
            # The current line is the title
            page_title = lines[line_cursor_position]
            line_cursor_position += 3
        else:
            # Set filename as the title
            page_title = os.path.basename(file_path)

        # HTML template
        doc.asis('<!DOCTYPE html>')
        with tag('html', lang='en'):
            with tag('head'):
                doc.stag('meta', charset="utf-8")
                with tag('title'):
                    text(page_title.replace("\n", ""))
                doc.stag('meta', name="viewport", content="width=device-width, initial-scale=1")

            with tag('body'):
                # File content here

                # Add an h1 if the title is present
                if is_title_present(lines):
                    with tag('h1'):
                        text(page_title.replace("\n", ""))

                # Continue with the remaining content
                while line_cursor_position < len(lines):
                    paragraph_content = ""

                    # Club paragraph content
                    while line_cursor_position < len(lines) and lines[line_cursor_position] != '\n':
                        paragraph_content += lines[line_cursor_position]
                        line_cursor_position += 1
                    
                    # Neutralize extra spaces/newlines from content
                    paragraph_content = paragraph_content.replace("\n", "").strip()
                    line_cursor_position += 1

                    if len(paragraph_content) > 1:
                        # Only add the paragraph tag if there is some content
                        with tag('p'):
                            text(paragraph_content)

    # print(indentation.indent(doc.getvalue()))
    file_content = indentation.indent(doc.getvalue())
    gen_file_path = f"{OUTPUT_PATH}/{os.path.basename(file_path)}"

    return File(gen_file_path, file_content)

def is_title_present(lines):
    return lines[0] != '\n' and \
        len(lines) > 1 and lines[1] == '\n' and \
        len(lines) > 2 and lines[2] == '\n'

def generate_files(files_to_be_generated):
    # Delete the output directory if it already exists
    if os.path.isdir(OUTPUT_PATH):
        # Delete the folder structure
        shutil.rmtree(OUTPUT_PATH)


    # Generate the output directory
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Generate an html file for each text file
    for file in files_to_be_generated:
        file.generate_html_file()
