# til-page-builder

A command-line tool for authoring "Today I Learned" posts in Markdown, which can be converted to HTML for publishing on the web.

<div align="center" style="width: 100%">
  <div style="display: flex; align-items: flex-start; justify-content: space-around;">
    <img width="150" src="./assets/bob_the_builder.png" alt="Bob the builder image">
    <img width="225" src="./assets/til_to_html.png" alt="TIL to HTML image">
  </div>
</div>

## Requirements 💻

**1. Python**

This tool requires Python 3 interpreter to be installed on user's system and added to the `PATH` system variable so that python files can be easily executed from the terminal.

**2. Packages**

This project only uses 1 external library that you need to install a package from PyPi called `yattag`
```
pip install yattag
```

Alternatively, all the dependencies used by project that need to be installed are configured in the `requirements.txt` file included in the project.

The following command installs all the dependencies configured in the requirements.txt file with corresponding versions.
```
pip install -r requirements.txt
```

## Usage

The driver file for this tool is located at `src/til-builder_main.py`. This is the file that needs to be executed for to perform all kinds of actions that the tool supports.

There are several ways in which you can use this tool.

### Default Behavior

At its core, the tool takes either a text file or a folder containing files as a positional argument and then generates corresponding html files to `./til` folder by default.

**Note:** The following commands assume that you are currently located in the src folder that contains the `til-builder_main.py` driver file.

1. Converting a file

```
python til-builder_main.py file.txt
```

2. Converting all files within a folder

```
python til-builder_main.py <folder path>
```

### Flags/Options for custom behavior

Here are some examples demonstrating usage of custom flags supported by the tool.

1. `-v` or `--version` : Displays the program name and the version that is in use.
```
python  .\src\til-builder_main.py --version
```

Output:

```
TIL Page Builder: 0.0.1
```

2. `-h` or `--help` : Displays a help message that describes usage of all kinds of commandline arguments supported.

```
python  .\src\til-builder_main.py --help
```

Output:
```
usage: TIL Page Builder [-h] [-o OUTPUT] [-v] [input_path]

Converts text files for TIL posts to HTML files for publishing on the web.

positional arguments:
  input_path            The path to a text file or a folder containing files to be converted to corresponding html file(s)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Generates the html files in the provided directory, by default it is './til'
  -v, --version         Show the name and version of the project
```

3. `-o` or `--output` : Generates the html files in the provided directory, by default it is './til'.

For example, in order to generate the html files in a directory `./dist/html_files`
```
python til-page_builder_main.py --output ./dist/html_files
```

## License

[MIT](https://github.com/Amnish04/til-page-builder/blob/master/LICENSE)

