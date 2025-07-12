""" "This module is responsible for integration testing of this application"""

import os
from snapshots import snapshots
from cli import App


class TestIntegration:
    """Integration testing suites"""

    DEFAULT_OUTPUT = "til"

    def test_general(self):
        """Compare the generated output with a sample file to verify general expectations"""

        # Load the exected html from snapshot
        expected_html = snapshots["yattag_html"]

        # Run the application with default settings
        app = App()
        app.run("integration/test_samples/til-yattag.md", test_context=True)

        # Verify if the file was generated in the correct location
        assert os.path.isfile(f"{TestIntegration.DEFAULT_OUTPUT}/til-yattag.html")

        # Verify the contents of generated file match with the expected snapshot
        with open(
            f"{TestIntegration.DEFAULT_OUTPUT}/til-yattag.html", "r"
        ) as generated_file:
            generated_html = generated_file.read()

            assert generated_html == expected_html
