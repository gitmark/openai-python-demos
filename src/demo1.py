#!/usr/bin/env python3
"""
demo1.py - Demonstrates basic usage of the OpenAI Python API client.

This script is uses an example from the OpenAI's github openai-python repository README.
It shows how to initialize the client with an API key (sourced from an environment variable),
make a request to generate a response using a specified model, and print the resulting output.
Additional comments have been added for educational purposes.
"""

import os
from openai import OpenAI

# Initialize the OpenAI client with the API key.
# The API key is retrieved from the environment variable 'OPENAI_API_KEY'.
# This key is required for authenticating API requests.
client = OpenAI(
    # The API key parameter is optional if already set as a default in your environment.
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Create a request to generate a response from the OpenAI API.
# The 'responses.create' method is used to send a prompt to the API.
# Parameters:
#   - model: Specifies the AI model to use (in this case, "gpt-4o").
#   - instructions: Provides the assistant's role or context (here, it is instructed to speak like a pirate).
#   - input: The query or prompt for which the assistant will generate a response.
response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

# Print the generated output text to the console.
print(response.output_text)
