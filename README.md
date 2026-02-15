# GitHub Markdown PDF

[![Tests](https://github.com/dhruvkej9/github-markdown-pdf/actions/workflows/test.yml/badge.svg)](https://github.com/dhruvkej9/github-markdown-pdf/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Get proper formatted PDF using Python without any problem! Convert GitHub flavored Markdown files to beautifully formatted PDFs with ease.

## Features

- 🔥 **GitHub Flavored Markdown**: Full support for GFM syntax
- 🎨 **Custom Styling**: Apply your own CSS styles to PDFs
- 🚀 **Batch Processing**: Convert multiple files at once
- 💻 **Command Line Interface**: Easy-to-use CLI tool
- 🐍 **Python API**: Programmatic access for integration
- ⚡ **Fast & Reliable**: Efficient conversion process

## Installation

```bash
pip install github-markdown-pdf
```

## Quick Start

### Command Line Usage

```bash
# Convert single file
md2pdf README.md

# Convert with custom output name
md2pdf README.md my-document.pdf

# Batch convert all markdown files in a directory
md2pdf docs/ --batch --output-dir pdfs/
```

### Python API Usage

```python
from github_markdown_pdf import MarkdownToPDFConverter

# Create converter
converter = MarkdownToPDFConverter()

# Convert single file
converter.convert('README.md', 'README.pdf')

# Batch convert
results = converter.batch_convert('docs/', 'pdfs/')
```

## Custom Styling

You can apply custom CSS styling to your PDFs:

```python
from github_markdown_pdf import MarkdownToPDFConverter

custom_css = """
body {
    font-family: 'Georgia', serif;
    color: #333;
}
h1 { color: #e74c3c; }
"""

converter = MarkdownToPDFConverter(custom_css=custom_css)
converter.convert('input.md', 'styled_output.pdf')
```

## Documentation

For detailed documentation, examples, and API reference, see the [docs/](docs/) directory.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/dhruvkej9/github-markdown-pdf.git
cd github-markdown-pdf

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who help improve this project
- Inspired by the need for better Markdown to PDF conversion tools
