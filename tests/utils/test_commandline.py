import sys
from unittest.mock import patch
from utils.commandline import CommandlineParser


class TestCommandline:
    class TestCommandlineParserWithArguments:
        """
        Tests for CommandLine
        """

        def test_arguments(self):
            # Prepare a list of command-line arguments
            arguments = [
                "-c",
                "config.toml",
                "input.md",
                "-o",
                "./output",
                "-l",
                "en-US",
                "-v",
            ]

            # Apply the patch to sys.argv to mimic command-line arguments
            with patch.object(sys, "argv", ["commandline.py"] + arguments):
                # Create an instance of the CommandlineParser
                parser = CommandlineParser()

                # Get the parsed arguments
                args = parser.get_args()

                # Assert that the arguments are correctly parsed
                assert args.config == "config.toml"
                assert args.input_path == "input.md"
                assert args.output == "./dist/til"
                assert args.version
