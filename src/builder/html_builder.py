from yattag import Doc, indentation

def generate_html_for_file(file_path):
    with open(file_path, "r") as file:
        # Create the html virtual document
        doc, tag, text = Doc().tagtext()

        # HTML template
        doc.asis('<!DOCTYPE html>')
        with tag('html', lang='en'):
            with tag('body'):
                with tag('p', id = 'main'):
                    text('some text')
                with tag('a', href='/my-url'):
                    text('some link')

        print(indentation.indent(doc.getvalue()))

        lines = file.readlines()
        # print(lines)