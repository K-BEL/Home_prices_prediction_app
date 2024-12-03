#!/bin/bash

# Install required Python packages
pip install numpy pandas scikit-learn

# Get the current working directory (project root)
PROJECT_ROOT=$(pwd)

# Define the folder path relative to the project root
FOLDER_PATH="$PROJECT_ROOT/server"

# Output the folder path
echo "Folder Path: $FOLDER_PATH"

# Run the Python script
python "$FOLDER_PATH/server.py"

# bash run.sh