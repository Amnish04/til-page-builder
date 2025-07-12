from typing import List
from builder.toc_generator.heading_item import HeadingItem


class TOC:
    def __init__(self, items: List["HeadingItem"] = None):
        self.items = [] if items is None else items

    def add_item(self, item: HeadingItem):
        self.items.append(item)

    def get_html(self):
        return f"""
            <div class="table-of-contents">
                <h2>Table of Contents</h2>
                <ul>
                    {"".join(list(map(lambda item: item.get_html(), self.items)))}
                </ul>
            </div>
            """

    def clear(self):
        self.items = []
