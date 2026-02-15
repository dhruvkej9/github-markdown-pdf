#!/usr/bin/env python3
"""
Setup script for GitHub Markdown PDF package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Read version from __init__.py
def get_version():
    """Get version from package __init__.py"""
    init_file = os.path.join("github_markdown_pdf", "__init__.py")
    with open(init_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "0.1.0"

setup(
    name="github-markdown-pdf",
    version=get_version(),
    author="dhruv kejriwal",
    author_email="",
    description="Get proper formatted PDF using Python without any problem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhruvkej9/github-markdown-pdf",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "flake8",
            "black",
            "isort",
            "mypy",
            "twine",
            "build",
        ],
    },
    entry_points={
        "console_scripts": [
            "md2pdf=scripts.md2pdf:main",
        ],
    },
    scripts=["scripts/md2pdf.py"],
    include_package_data=True,
    zip_safe=False,
    keywords="markdown pdf converter github",
    project_urls={
        "Bug Reports": "https://github.com/dhruvkej9/github-markdown-pdf/issues",
        "Source": "https://github.com/dhruvkej9/github-markdown-pdf",
        "Documentation": "https://github.com/dhruvkej9/github-markdown-pdf#readme",
    },
)