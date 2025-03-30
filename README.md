# OpenAI API Python Demos

This repository is dedicated to exploring and demonstrating the usage of [OpenAI's Python API](https://github.com/openai/openai-python). Here, you'll find a collection of examples, explanations, and demos that build on the official API examples.

## Overview

- **Purpose**: To provide clear, commented examples and demonstrations of how to use OpenAI's Python API.
- **Content**: Includes demo scripts (e.g., `demo_01.py`, `demo_02.py`, etc.) based on examples from the official OpenAI README, with additional commentary and explanations.
- **Future Plans**: More examples and custom implementations will be added over time, along with deeper explanations to help you better understand the API.

## Installation

You can install the OpenAI Python library using pip (compatible with Linux and other platforms):

```bash
pip install openai
```

Ensure you have a working Python environment before installation.

# [Demo Scripts](https://github.com/gitmark/openai-python-demos/blob/main/docs/demos.md)

- **demo_01.py**: Response API.
- **demo_02.py**: Chat Completion API
- (etc.)



Feel free to run and modify these scripts to experiment with the API and learn by example.

# Additional Resources

For more detailed documentation and further reading, check out these resources:

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [Quickstart Guide (Chat API Mode)](https://platform.openai.com/docs/quickstart?api-mode=chat)
- [OpenAI Python Library Documentation](https://platform.openai.com/docs/libraries?language=python)
- [Guide to Agents](https://platform.openai.com/docs/guides/agents)

# Contributing

Contributions, bug reports, and feature requests are welcome! 
Feel free to open issues if you have suggestions or encounter any problems.

# License

Distributed under the MIT License. See the `LICENSE` file for more information.


# Project Link

[openai-python-demos](https://github.com/gitmark/openai-python-demos)

#####

To run all the python demos execute:
```bash
./run_demos.sh
```

The first python script called by this main script is demo_01.py which asks the OpenAI API to respond like a pirate, giving results similar to:

Arrr, ye be usin' the `isinstance()` function fer that task, matey! Ye just need to provide the object and the class ye be checkin'. Here be the way to do it:

```python
if isinstance(your_object, YourClass):
    print("Aye, 'tis an instance of the class!")
else:
    print("Nay, 'tis not.")
```

Go forth and code like a true buccaneer! 🏴‍☠️