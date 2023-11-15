import os
import re
from yattag import Doc, indentation
from models.html_file import HtmlFile

from utils.helper_functions import has_txt_extension, has_md_extension
from utils.commandline import CommandlineParser
import builder.line_queries as line_queries

from builder.toc_generator.toc import TOC, HeadingItem


class HtmlBuilder:
    """Functionality to build and generate the html documents"""

    TOC_PLACEHOLDER = '<div id="toc-placeholder"></div>'

    def __init__(self):
        self._cl_args = CommandlineParser().get_args()

        self._output_path = self._cl_args.output  # Output directory for files
        self._document_lang = self._cl_args.lang  # Language used for the document

        # TOC Object
        self.toc = TOC()

    def generate_html_file_object(self, file_path):
        """Reads file at path provided and generates an `HtmlFile` object with corresponding html

        :param file_path: _description_
        :return: _description_
        """
        # Start with a clean slate
        self.reset()

        with open(file_path, "r") as file:
            # Create the html virtual document
            virtual_doc = Doc().tagtext()

            # pylint: disable=unused-variable
            # This is required for tuple unpacking
            doc, tag, text = virtual_doc
            # pylint: enable=unused-variable

            lines = file.readlines()

            # Check for a title
            if self._is_title_present(lines):
                # The current line is the title
                page_title = lines[0]
            else:
                # Set filename as the title
                page_title = os.path.basename(file_path)

            # HTML template
            self.generate_document_content(virtual_doc, page_title, lines, file_path)

        file_content = doc.getvalue()  # Get the generated html string
        file_content = file_content.replace(
            HtmlBuilder.TOC_PLACEHOLDER, self.toc.get_html()
        )  # Replace TOC placeholder with actual TOC
        file_content = indentation.indent(file_content)  # Indent the html

        gen_file_path = f"{self._output_path}/{os.path.basename(file_path)}"

        return HtmlFile(gen_file_path, file_content)

    def reset(self):
        """Reset the state of the builder"""
        self.toc.clear()

    def generate_document_content(
        self, virtual_doc, page_title, lines, input_file_path
    ):
        doc, tag, text = virtual_doc
        line_cursor_position = 0

        doc.asis("<!DOCTYPE html>")
        with tag("html", lang=self._document_lang):
            with tag("head"):
                doc.stag("meta", charset="utf-8")
                with tag("title"):
                    text(self._neutralize_newline_character(page_title))
                doc.stag(
                    "meta",
                    name="viewport",
                    content="width=device-width, initial-scale=1",
                )

            with tag("body"):
                # Add an h1 if the title is present
                if has_txt_extension(input_file_path) and self._is_title_present(lines):
                    with tag("h1"):
                        text(self._neutralize_newline_character(page_title))
                        line_cursor_position += 3

                # Placeholder for TOC
                with tag("div", id="toc-placeholder"):
                    doc.asis()

                # Continue with the remaining content
                while line_cursor_position < len(lines):
                    text_block = ""

                    # Club paragraph content
                    while (
                        line_cursor_position < len(lines)
                        and lines[line_cursor_position] != "\n"
                    ):
                        text_block += lines[line_cursor_position]
                        line_cursor_position += 1

                    # Neutralize extra spaces/newlines from content
                    text_block = self._neutralize_newline_character(text_block).strip()
                    line_cursor_position += 1

                    if len(text_block) > 1:
                        if has_md_extension(input_file_path):
                            self._process_text_block_for_markdown(
                                virtual_doc, text_block
                            )
                        else:
                            # No additional processing for text files
                            with tag("p"):
                                text(text_block)

    def _process_text_block_for_markdown(self, virtual_doc, text_block):
        """
        Processes the provided text block and appends it to the doc instance provided

        :param virtual_doc: An instance of Yattag virtual document
        :param text_block: Block of text to be processed
        """
        # pylint: disable=unused-variable
        doc, tag, text = virtual_doc
        # pylint: enable=unused-variable

        # Move from inner to outer tags when processing

        # Inline elements
        # Use regEx to replace markdown bold format (*** ***) with html <strong><em> <em/></strong> tags
        text_block = re.sub(
            r"\*\*\*(.*?)\*\*\*", r"<strong><em>\1</em></strong>", text_block
        )
        # Use regEx to replace markdown bold format (** **) with html <strong> </strong> tags
        text_block = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text_block)
        # Use regEx to replace markdown italic format (* * or _ _) with html <em> </em> tags
        text_block = re.sub(r"(\*|_)(.*?)\1", r"<em>\2</em>", text_block)

        # Block level elements
        if line_queries.is_h1(
            text_block,
        ):
            formatted_block = text_block.replace(line_queries.H1_TOKEN, "")

            with tag("h1", id=HeadingItem.generate_heading_id(formatted_block)):
                doc.asis(formatted_block)
        elif line_queries.is_h2(text_block):
            formatted_block = text_block.replace(line_queries.H2_TOKEN, "")

            with tag("h2", id=HeadingItem.generate_heading_id(formatted_block)):
                doc.asis(formatted_block)
                self.toc.add_item(HeadingItem(formatted_block))
        elif line_queries.is_h3(text_block):
            formatted_block = text_block.replace(line_queries.H3_TOKEN, "")

            with tag("h3", id=HeadingItem.generate_heading_id(formatted_block)):
                doc.asis(formatted_block)
                self.toc.add_item(HeadingItem(formatted_block))
        elif line_queries.is_h4(text_block):
            formatted_block = text_block.replace(line_queries.H4_TOKEN, "")

            with tag("h4", id=HeadingItem.generate_heading_id(formatted_block)):
                doc.asis(formatted_block)
                self.toc.add_item(HeadingItem(formatted_block))
        elif line_queries.is_h5(text_block):
            formatted_block = text_block.replace(line_queries.H5_TOKEN, "")

            with tag("h5", id=HeadingItem.generate_heading_id(formatted_block)):
                doc.asis(formatted_block)
                self.toc.add_item(HeadingItem(formatted_block))
        elif line_queries.is_h6(text_block):
            formatted_block = text_block.replace(line_queries.H6_TOKEN, "")

            with tag("h6", id=HeadingItem.generate_heading_id(formatted_block)):
                doc.asis(formatted_block)
                self.toc.add_item(HeadingItem(formatted_block))
        else:
            with tag("p"):
                doc.asis(text_block)

    def _is_title_present(self, lines):
        """Takes the list of lines in a file, returns True if the first line is title"""
        return (
            lines[0] != "\n"
            and len(lines) > 1
            and lines[1] == "\n"
            and len(lines) > 2
            and lines[2] == "\n"
        )

    def _neutralize_newline_character(self, line):
        """Removes any line delimeters like line feeds (\n) or carriage returns (\r\n), returns the cleaned line"""

        cleaned_line = line.replace("\r\n", "").replace("\n", "")
        return cleaned_line
