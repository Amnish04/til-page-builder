import os
import shutil
from yattag import Doc, indentation
from utils.commandline import cl_args
from models.file import File

from utils.helper_functions import has_txt_extension, has_md_extension
from builder.markdown_processor import process_text_block_for_markdown

# Global variables
OUTPUT_PATH = cl_args.output # Output directory for files
DOCUMENT_LANG = cl_args.lang # Language used for the document
FILES_TO_BE_GENERATED = []   # A list of File objects

def generate_html_for_file(file_path):

    with open(file_path, "r") as file:
        # Create the html virtual document
        virtual_doc = Doc().tagtext()
        doc, tag, text = virtual_doc

        lines = file.readlines()
        line_cursor_position = 0

        # Check for a title
        if is_title_present(lines):
            # The current line is the title
            page_title = lines[line_cursor_position]
        else:
            # Set filename as the title
            page_title = os.path.basename(file_path)

        # HTML template
        doc.asis('<!DOCTYPE html>')
        with tag('html', lang=DOCUMENT_LANG):
            with tag('head'):
                doc.stag('meta', charset="utf-8")
                with tag('title'):
                    text(neutralize_newline_character(page_title))
                doc.stag('meta', name="viewport", content="width=device-width, initial-scale=1")

            with tag('body'):
                # File content here

                # Add an h1 if the title is present
                if has_txt_extension(file_path) and is_title_present(lines):
                    with tag('h1'):
                        text(neutralize_newline_character(page_title))
                        line_cursor_position += 3

                # Continue with the remaining content
                while line_cursor_position < len(lines):
                    text_block = ""

                    # Club paragraph content
                    while line_cursor_position < len(lines) and lines[line_cursor_position] != '\n':
                        text_block += lines[line_cursor_position]
                        line_cursor_position += 1
                    
                    # Neutralize extra spaces/newlines from content
                    text_block = neutralize_newline_character(text_block).strip()
                    line_cursor_position += 1

                    if len(text_block) > 1:
                        if has_md_extension(file_path):
                            process_text_block_for_markdown(virtual_doc, text_block)
                        else:
                            # No additional processing for text files
                            with tag('p'):
                                text(text_block)

                    

    file_content = indentation.indent(doc.getvalue())
    gen_file_path = f"{OUTPUT_PATH}/{os.path.basename(file_path)}"

    return File(gen_file_path, file_content)

def is_title_present(lines):
    """Takes the list of lines in a file, returns True if the first line is title"""
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

def neutralize_newline_character(line):
    """Removes any line delimeters like line feeds (\n) or carriage returns (\r\n), returns the cleaned line"""

    cleaned_line = line.replace('\r\n', '').replace('\n', '')
    return cleaned_line
