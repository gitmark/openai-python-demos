#!/bin/bash

# Initialize virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    
    # Activate virtual environment
    source venv/bin/activate
    pip3 install openai
else
    # Activate virtual environment
    source venv/bin/activate
fi

python3 demo1.py
