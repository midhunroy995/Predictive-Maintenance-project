import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

# Define project name
project_name = "MachineFailurePrediction"

# Define list of files and directories to create
list_of_files = [
    # GitHub workflows
    ".github/workflows/.gitkeep",
    # Source code directories
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/notebooks/__init__.py",
    f"src/{project_name}/scripts/__init__.py",
    f"src/{project_name}/scripts/preprocess.py",
    f"src/{project_name}/scripts/train.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    # Configuration files
    "config/config.yaml",
    "params.yaml",
    # Application files
    "app.py",
    "main.py",
    # Dockerfile and requirements
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    # Research and testing files
    "research/trials.ipynb",
    "tests/test_pipeline.py",
    # Logging file
    "logs/logging.txt"
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

