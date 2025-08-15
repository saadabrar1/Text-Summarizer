import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

version = "0.0.0"  

REPO_NAME = "Text-Summarizer"
AUTHOR = "saadabrar1"
SRC_REPO = "textSummarizer"
EMAIL = "saadabbasi5665@gmail.com"


setuptools.setup (
    name=SRC_REPO,  # The package name users will install (pip install textSummarizer)
    version=version,
    author=AUTHOR,
    author_email=EMAIL,
    description="A text summarization project using NLP",
    long_description=long_description,  # Uses README.md content
    long_description_content_type="text/markdown",  # PyPI expects markdown
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",  # Your GitHub repo link
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
)