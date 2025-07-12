from setuptools import setup, find_packages
from src.til_page_builder.version import __version__ as version

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="til_page_builder",
    version=version,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "til_page_builder=til_page_builder.cli:main",  # Adjust 'module_name' and 'main' accordingly
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="Amnish Singh Arora",
    author_email="amnishsingh04@gmail.com",
    description="A command-line tool for authoring 'Today I Learned' posts in Markdown, which can be converted to HTML for publishing on the web.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Homepage": "https://github.com/pypa/sampleproject",
        "Issues": "https://github.com/pypa/sampleproject/issues",
    },
)
