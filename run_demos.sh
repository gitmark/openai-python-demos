#!/bin/bash

# Initialize virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    # Optional: Upgrade pip
    pip install --upgrade pip
    # (future change) pip install -r requirements.txt
    pip3 install openai
else
    echo "Activating existing virtual environment..."
    source venv/bin/activate
fi

# Run the demo script
python3 openai_demos/demo1.py

# Deactivate the virtual environment
deactivate
