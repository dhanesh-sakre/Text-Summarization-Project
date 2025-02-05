from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Text-Summarization-Project"
AUHTOR_USER_NAME = "dhanesh-sakre"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "dhaneshsakre@gmail.com"

setup(
    name=SRC_REPO,
    version="0.0.0",
    author=AUHTOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for NLP app.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUHTOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug Tracker" : f"https://github.com/{AUHTOR_USER_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)