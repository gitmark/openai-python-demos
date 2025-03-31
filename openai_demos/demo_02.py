#!/usr/bin/env python3
"""
demo_02.py - Demonstrates the usage of the Chat Completions API with the OpenAI Python API client.

This script shows how to simulate a conversation with the AI by structuring a dialogue
using different roles (e.g., "developer" and "user"). The example instructs the AI to talk like a pirate
while answering a coding question about checking an object's instance in Python.
"""

from openai import OpenAI

# Print a title to indicate the demo being executed.
print("Demo 02 - Chat Completions API")

# Initialize the OpenAI client.
# Note: We are not explicitly providing an API key here,
# so it is assumed that the API key is already configured in your environment.
client = OpenAI()

# Create a chat completion request.
# The 'chat.completions.create' method is used to simulate a conversation.
# It accepts a list of messages that provide context and instructions to the AI.
completion = client.chat.completions.create(
    model="gpt-4o",  # Specify the model to be used for generating the response.
    messages=[
        # The first message sets the context by instructing the assistant to "Talk like a pirate."
        {"role": "developer", "content": "Talk like a pirate."},
        # The second message provides the user's query regarding checking an object's instance in Python.
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

# Extract and print the generated response from the conversation.
# The response is located in the first choice's message content.
print(completion.choices[0].message.content + "\n")
