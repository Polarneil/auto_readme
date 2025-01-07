# Code Repository Analysis and README Generator

This repository contains a Python script that automates the process of cloning code repositories, analyzing their contents, and generating a professional `README.md` file using OpenAI's services. The script is designed to handle various code file types, making it a versatile tool for developers looking to streamline documentation creation.

## Project Overview

The main goal of this project is to facilitate the automatic generation of high-quality `README.md` files for various code repositories. By leveraging the power of OpenAI's API, the script analyzes the structure and main components of a given repository to produce detailed documentation that can be used for presentation or distribution of the project's code.

The process involves:
1. Cloning a specified code repository.
2. Analyzing the contents of the repository to summarize key files.
3. Generating a prompt and using OpenAI to produce a professional-grade `README.md`.

## Installation Instructions

To run this project, you need to have Python installed along with the necessary dependencies. Follow the steps below to get started:

1. **Clone This Repository:**
   ```
   git clone https://github.com/Polarneil/auto_readme.git
   cd <repository_directory>
   ```

2. **Install the Required Packages:**
   Ensure you have `pip` installed and use it to install the required packages specified in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

## Usage

Once you have the environment set up and dependencies installed, you can use the script as follows:

1. **Clone and Analyze a Repository:**
   - Open and run `readme.py`.
   - Pass the URL of the repository you want to clone and analyze to the `clone_repo` function. The repository will be cloned into a default path (`../repos/`).

2. **Generate the README.md:**
   - The script automatically analyzes the repository's structure and contents, generating a `README.md` inspired by the files in the codebase.

Example of how to run within a Python environment:

```python
from readme import clone_repo, analyze_repo, generate_prompt

repo_url = "https://github.com/user/repo_name"
clone_path = clone_repo(repo_url)
repo_summary = analyze_repo(clone_path)
prompt = generate_prompt(repo_summary)

# Use the generated prompt to create a README with OpenAI API
```

## Contribution Guidelines

Contributions to this project are welcome. Here are some ways to contribute:

- **Bug Reports**: Report any bugs or issues you encounter.
- **Feature Requests**: Suggest new features that could enhance the project's capabilities.
- **Code Contributions**: Submit pull requests for bug fixes or new features. Please ensure code contributions are well-documented and adhere to Python's best practices.
- **Documentation**: Help improve the documentation for better clarity and usability.

Before contributing, please make sure to discuss the change via an issue or email with the owners of this repository.

---

Feel free to become a part of this evolving project, and thank you for your interest and contributions!