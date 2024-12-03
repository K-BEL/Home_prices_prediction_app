#!/bin/bash

# Install required Python packages
pip install flask flask-openapi3 pydantic flask-cors
pip install numpy pandas scikit-learn

# Get the current working directory (project root)
PROJECT_ROOT=$(pwd)

# Define the folder path relative to the project root
FOLDER_PATH="$PROJECT_ROOT/server"

# Output the folder path
echo "Folder Path: $FOLDER_PATH"

# Run the Python script
streamlit run "$FOLDER_PATH/app.py"

# bash run_str.sh