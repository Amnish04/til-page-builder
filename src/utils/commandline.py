import argparse
import tomli

class CommandlineParser:
    _instance = None

    def __new__(cls):
        """Restrict the instantiation class to a single instance

        :return: A global point of access to the single instance
        """
        if cls._instance is None:
            cls._instance = super(CommandlineParser, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        # Create an ArgumentParser object
        self._parser = argparse.ArgumentParser(
                    prog='TIL Page Builder',
                    description='Converts text files for TIL posts to HTML files for publishing on the web.',
                    )
        self._setup_arguments()

    def get_args(self):
        return self._cl_args

    def _setup_arguments(self):
        # Define supported arguments

        # Config file
        self._parser.add_argument(
            '-c','--config',
            metavar='config',
            type=str,
            help="Uses a provided config file to set any valid options for the program."
        )

        # Input file or folder containing files
        self._parser.add_argument(
            'input_path',
            default=None,
            nargs='?',
            help="The path to a text file or a folder containing files to be converted to corresponding html file(s)"
        )

        # Output directory
        self._parser.add_argument(
            '-o', '--output',
            default="./til",
            type=str,
            help="Generates the html files in the provided directory, by default it is './til'"
        )

        # Lang attribute
        self._parser.add_argument(
            '-l', '--lang',
            default="en-CA",
            type=str,
            help="Indicates the language to use when generating the lang attribute on the root element"
        )

        # Display project version
        self._parser.add_argument(
            '-v', '--version',
            action='store_true',
            help="Show the name and version of the project"
        )  # on/off flag

        # Parse the command-line arguments
        self._cl_args = self._parser.parse_args()

        self._process_config_file()

        
    def _process_config_file(self):
        """Process the config file if provided"""
        if self._cl_args.config is not None:
            with open(self._cl_args.config, 'rb') as config_file:     # Opening config file
                try:
                    toml_vals = tomli.load(config_file)       # Loading configurations from TOML file
                except tomli.TOMLDecodeError:
                    raise Exception("Error: Unable to decode configuration file contents")
                except:
                    raise Exception("Error: Invalid configuration file")

            for (key,value) in toml_vals.items():      
                setattr(self._cl_args, key, value)       # Setting each attribute in arg namespace from tomli dictionary
