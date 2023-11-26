"""This file contains functions that check if a line is of certain type"""

# Constants
H1_TOKEN = "# "
H2_TOKEN = "## "
H3_TOKEN = "### "
H4_TOKEN = "#### "
H5_TOKEN = "##### "
H6_TOKEN = "###### "

# Functions


def is_h1(line):
    """Returns True if the provided line starts with '# '"""
    return line.startswith(H1_TOKEN)


def is_h2(line):
    """Returns True if the provided line starts with '## '"""
    return line.startswith(H2_TOKEN)


def is_h3(line):
    """Returns True if the provided line starts with '### '"""
    return line.startswith(H3_TOKEN)


def is_h4(line):
    """Returns True if the provided line starts with '#### '"""
    return line.startswith(H4_TOKEN)


def is_h5(line):
    """Returns True if the provided line starts with '##### '"""
    return line.startswith(H5_TOKEN)


def is_h6(line):
    """Returns True if the provided line starts with '###### '"""
    return line.startswith(H6_TOKEN)
