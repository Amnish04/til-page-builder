import builder.line_queries as line_queries
import re

def process_text_block_for_markdown(virtual_doc, text_block):
    doc, tag, text = virtual_doc
    # Move from inner to outer tags when processing

    # Inline elements
    # Use regEx to replace markdown bold format (*** ***) with html <strong><em> <em/></strong> tags
    text_block = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text_block)
    # Use regEx to replace markdown bold format (** **) with html <strong> </strong> tags
    text_block = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text_block)
    # Use regEx to replace markdown italic format (* * or _ _) with html <em> </em> tags
    text_block = re.sub(r'(\*|_)(.*?)\1', r'<em>\2</em>', text_block)

    # Block level elements
    if line_queries.is_h1(text_block):
        with tag('h1'):
            doc.asis(text_block.replace(line_queries.H1_TOKEN, ""))
    elif line_queries.is_h2(text_block):
        with tag('h2'):
            doc.asis(text_block.replace(line_queries.H2_TOKEN, ""))
    elif line_queries.is_h3(text_block):
        with tag('h3'):
            doc.asis(text_block.replace(line_queries.H3_TOKEN, ""))
    elif line_queries.is_h4(text_block):
        with tag('h4'):
            doc.asis(text_block.replace(line_queries.H4_TOKEN, ""))
    elif line_queries.is_h5(text_block):
        with tag('h5'):
            doc.asis(text_block.replace(line_queries.H5_TOKEN, ""))
    elif line_queries.is_h6(text_block):
        with tag('h6'):
            doc.asis(text_block.replace(line_queries.H6_TOKEN, ""))
    else:
        with tag('p'):
            doc.asis(text_block)
