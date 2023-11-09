"""This module defined HeadingItem class"""

from typing import List
import hashlib


class HeadingItem:
    """Represents a heading item in a TOC (Table of contents)"""

    # Class Variables
    DEFAULT_CHILDREN_VALUE = []
    DEFAULT_HEADING_VALUE = ""

    def __init__(self, value: str = None, children: List["HeadingItem"] = None):
        """Constructor

        :param id: id of the corresponding html element
        :param value: inner html of the corresponding html element
        :param children: child nodes
        """
        self.value = HeadingItem.DEFAULT_HEADING_VALUE if value is None else value
        self.id = HeadingItem.generate_heading_id(self.value)
        self.children = (
            HeadingItem.DEFAULT_CHILDREN_VALUE if children is None else children
        )

    @staticmethod
    def generate_heading_id(text_content: str):
        """Generate a unique hash id based on the heading text

        :param text_content: Text content of the heading
        :return: A unique `sha512` id for the heading
        """
        # Create a SHA-512 hash object
        sha512_hash = hashlib.sha512()

        # Update the hash object with the bytes of the string
        sha512_hash.update(text_content.encode())

        # Get the hexadecimal representation of the hash
        return sha512_hash.hexdigest()

    def get_html(self) -> str:
        """
        Return corresponding html for the object
        """

        return f"""
            <li>
                <a href='#{self.id}'>{self.value}</a>
            </li>
            """
