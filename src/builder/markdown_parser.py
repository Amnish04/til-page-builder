import os
import shutil
from yattag import Doc, indentation
from utils.commandline import cl_args
from models.file import File

import builder.line_queries as line_queries

def generate_markdown(file_path):
