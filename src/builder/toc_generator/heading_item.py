"""This module defined HeadingItem class"""

from typing import List
import hashlib


class HeadingItem:
    """Represents a heading item in a TOC (Table of contents)"""

    # Class Variables
    CHILDREN_DEFAULT_VALUE = []

    def __init__(self, value: str, children: List["HeadingItem"] = None):
        """Constructor

        :param id: id of the corresponding html element
        :param value: inner html of the corresponding html element
        :param children: child nodes
        """
        self.id = HeadingItem.generate_heading_id(value)
        self.value = value
        self.children = (
            HeadingItem.CHILDREN_DEFAULT_VALUE if children is None else children
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
        return f"""
            <li>
                <a href='#{self.id}'>{self.value}</a>
            </li>
            """
