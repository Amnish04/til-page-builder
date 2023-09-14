import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(
                    prog='TIL Page Builder',
                    description='Converts text files for TIL posts to HTML files for publishing on the web.',
                    )

# Define arguments

# Input file or folder containing files
parser.add_argument(
    'input_path',
    default=None,
    nargs='?',
    help="Sets the output directory for generated html files to the specified path. By default, it is './til'"
)

# Output directory
parser.add_argument(
    '-o', '--output',
    default="./til",
    type=str,
    help="Sets the output directory for generated html files to the specified path. By default, it is './til'"
)

# Display project version
parser.add_argument(
    '-v', '--version',
    action='store_true',
    help="Show the name and version of the project"
)  # on/off flag

# Parse the command-line arguments
cl_args = parser.parse_args()
