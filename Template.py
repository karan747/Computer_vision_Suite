import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Computer_vision_Suite'

list_of_files = [
    ".github/workflow/.gitkeep/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/pages/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/assets/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/artifacts/__init__.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "Readme.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = os.path.dirname(filepath)
    if (filedir is not '') and (not os.path.exists(filedir)):
        os.makedirs(filedir)
        logging.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:
            logging.info(f"Created file: {filepath}")
            pass

    else:
        logging.info(f"File already exists: {filepath}")
