# openai-python-demos
OpenAI API Python Demos

This repository is dedicated to exploring and demonstrating the usage of [OpenAI's Python API](https://github.com/openai/openai-python). Here, you'll find a collection of examples, explanations, and demos that build on the official API examples.

## Overview

- **Purpose**: To provide clear, commented examples and demonstrations of how to use OpenAI's Python API.
- **Content**: Includes demo scripts (e.g., `demo1.py`, `demo2.py`, etc.) based on examples from the official OpenAI README, enhanced with additional commentary and explanations.
- **Future Plans**: More examples and custom implementations will be added over time, along with deeper explanations to help you better understand the API.

## Installation

Install the OpenAI Python library using pip (compatible with Linux and other platforms):

```bash
pip install openai
```

Ensure you have a working Python environment before installation.

# Demo Scripts

- **demo1.py**: A basic demonstration of using the OpenAI API.
- **demo2.py**: More advanced usage examples showcasing additional features.

Feel free to run and modify these scripts to experiment with the API and learn by example.

# Additional Resources

For more detailed documentation and further reading, check out these resources:

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [Quickstart Guide (Chat API Mode)](https://platform.openai.com/docs/quickstart?api-mode=chat)
- [OpenAI Python Library Documentation](https://platform.openai.com/docs/libraries?language=python)
- [Guide to Agents](https://platform.openai.com/docs/guides/agents)

# Contributing

Contributions, bug reports, and feature requests are welcome! To contribute:

1. Fork this repository.
2. Create a new branch for your changes.
3. Submit a pull request with a clear description of your changes.

Feel free to open issues if you have suggestions or encounter any problems.

# License

Distributed under the MIT License. See the `LICENSE` file for more information.


# Project Link

[https://github.com/gitmark/openai-python-demos](https://github.com/gitmark/openai-python-demos)

#####

To run all the python demos execute:
```bash
src/run_demos.sh
```

The first python script this main script will call is demo1.py which asks the openai API to respond like a pirate, resulting the results similar to:

Arrr, ye be usin' the `isinstance()` function fer that task, matey! Ye just need to provide the object and the class ye be checkin'. Here be the way to do it:

```python
if isinstance(your_object, YourClass):
    print("Aye, 'tis an instance of the class!")
else:
    print("Nay, 'tis not.")
```

Go forth and code like a true buccaneer! 🏴‍☠️