# GitHub Markdown PDF Documentation

Welcome to the GitHub Markdown PDF documentation!

## Overview

GitHub Markdown PDF is a Python package that converts GitHub flavored Markdown files to properly formatted PDF documents.

## Features

- **GitHub Flavored Markdown**: Full support for GitHub's markdown syntax
- **Custom Styling**: Apply custom CSS styles to your PDFs
- **Batch Processing**: Convert multiple markdown files at once
- **Command Line Interface**: Easy-to-use CLI tool
- **Python API**: Programmatic access for integration

## Quick Start

### Installation

```bash
pip install github-markdown-pdf
```

### Basic Usage

#### Command Line

```bash
md2pdf input.md output.pdf
```

#### Python API

```python
from github_markdown_pdf import MarkdownToPDFConverter

converter = MarkdownToPDFConverter()
converter.convert('input.md', 'output.pdf')
```

## Advanced Usage

### Custom CSS Styling

```python
from github_markdown_pdf import MarkdownToPDFConverter

# Using custom CSS string
custom_css = """
body {
    font-family: 'Times New Roman', serif;
    color: #333;
}
"""

converter = MarkdownToPDFConverter(custom_css=custom_css)
converter.convert('input.md', 'styled_output.pdf')
```

### Batch Processing

```python
from github_markdown_pdf import MarkdownToPDFConverter

converter = MarkdownToPDFConverter()
results = converter.batch_convert('markdown_files/', 'pdf_output/')
```

## API Reference

### MarkdownToPDFConverter

Main class for converting markdown to PDF.

#### Methods

- `convert(markdown_path, output_path=None, **options)`: Convert single file
- `batch_convert(input_dir, output_dir=None, pattern="*.md")`: Convert multiple files

## Examples

See the `examples/` directory for more detailed usage examples.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details.