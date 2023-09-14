import os
from yattag import Doc, indentation

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
                    with tag('p'):
                        text(lines[line_cursor_position].replace("\n", ""))
                        line_cursor_position += 1

    print(indentation.indent(doc.getvalue()))
    return indentation.indent(doc.getvalue())

def is_title_present(lines):
    return lines[0] != '\n' and \
        len(lines) > 1 and lines[1] == '\n' and \
        len(lines) > 2 and lines[2] == '\n'
