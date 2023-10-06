import argparse
import tomli

# Create an ArgumentParser object
parser = argparse.ArgumentParser(
                    prog='TIL Page Builder',
                    description='Converts text files for TIL posts to HTML files for publishing on the web.',
                    )

# Define arguments

# Config file
parser.add_argument(
    '-c','--config',
    metavar='config',
    type=str,
    help="Uses a provided config file to set any valid options for the program."
)

# Input file or folder containing files
parser.add_argument(
    'input_path',
    default=None,
    nargs='?',
    help="The path to a text file or a folder containing files to be converted to corresponding html file(s)"
)

# Output directory
parser.add_argument(
    '-o', '--output',
    default="./til",
    type=str,
    help="Generates the html files in the provided directory, by default it is './til'"
)

# Lang attribute
parser.add_argument(
    '-l', '--lang',
    default="en-CA",
    type=str,
    help="Indicates the language to use when generating the lang attribute on the root element"
)

# Display project version
parser.add_argument(
    '-v', '--version',
    action='store_true',
    help="Show the name and version of the project"
)  # on/off flag

# Parse the command-line arguments
cl_args = parser.parse_args()

# Processing config file if provided

if cl_args.config is not None:
    with open(cl_args.config, 'rb') as config_file:     # Opening config file
        try:
            toml_vals = tomli.load(config_file)       # Loading configurations from TOML file
        except tomli.TOMLDecodeError:
            raise Exception("Error: Unable to decode configuration file contents")
        except:
            raise Exception("Error: Invalid configuration file")

    for (key,value) in toml_vals.items():      
        setattr(cl_args, key, value)       # Setting each attribute in arg namespace from tomli dictionary