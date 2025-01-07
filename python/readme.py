import os
import git
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)


# Clone repo
def clone_repo(repo_url, clone_path="../repos/"):
    if os.path.exists(clone_path):
        os.system(f"rm -rf {clone_path}")
    git.Repo.clone_from(repo_url, clone_path)
    return clone_path


# Analyze repo
def analyze_repo(repo_path):
    repo_summary = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.go', '.html', '.css', 'Dockerfile', '.ipynb', '.csv', '.txt')):
                with open(os.path.join(root, file), 'r') as f:
                    repo_summary[file] = f.read()[:1000]  # Limit to first 1000 chars
    return repo_summary


# Generate prompt
def generate_prompt(repo_summary):
    prompt = "Generate a professional README.md for the following code repository.\n\n"
    for file, content in repo_summary.items():
        prompt += f"File: {file}\nContent:\n{content}\n\n"
    prompt += "Provide a project overview, installation instructions, usage, and contribution guidelines."
    return prompt


# Use OpenAI API
def generate_readme(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content


# Main function
def main(repo_url):
    repo_path = clone_repo(repo_url)
    repo_summary = analyze_repo(repo_path)
    prompt = generate_prompt(repo_summary)
    readme_content = generate_readme(prompt)

    with open(os.path.join(repo_path, "README.md"), 'w') as f:
        f.write(readme_content)

    print("README.md created successfully!")


# Example usage
if __name__ == "__main__":
    main("https://github.com/Polarneil/pandas.git")
