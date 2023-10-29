from typing import List
from builder.toc_generator.heading_item import HeadingItem

class TOC:
    def __init__(self, items: List['HeadingItem'] = []):
        self.items = items

    def add_item(self, item: HeadingItem):
        self.items.append(item)

    def get_html(self):
        return f"""
            <h2>Table of Contents</h2>
            <ul>
                {''.join(list(map(lambda item: item.get_html(), self.items)))}
            </ul>
            """
    
    def clear(self):
        self.items = []