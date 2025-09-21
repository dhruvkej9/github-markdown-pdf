# GitHub Markdown PDF Converter

GitHub Markdown PDF Converter is a Python application that converts markdown files to properly formatted PDF documents without common formatting issues. The project uses libraries like WeasyPrint, markdown, and other PDF generation tools.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap, Build, and Test the Repository

Install required dependencies and set up the development environment:

- `pip install --user markdown pdfkit weasyprint reportlab` -- takes 20-30 seconds. NEVER CANCEL. Set timeout to 60+ seconds.
- `pip install --user pytest black flake8` -- takes 15-20 seconds. NEVER CANCEL. Set timeout to 60+ seconds.

### Validate Installation

Always run this validation after setting up dependencies:

```python
python3 -c "
import markdown
import weasyprint
import pytest
import black
import flake8
print('✓ All required libraries installed successfully')
"
```

This validation takes less than 1 second and should always pass.

### Development Workflow

- Format code: `black .` -- takes 1-2 seconds
- Lint code: `flake8 .` -- takes 1-2 seconds  
- Run tests: `pytest -v` -- takes 2-3 seconds for basic tests. NEVER CANCEL. Set timeout to 30+ seconds for larger test suites.

### Manual Validation

Always manually validate any new markdown-to-PDF conversion code:

1. Create a test markdown file with common elements (headers, lists, code blocks, tables)
2. Run the conversion 
3. Verify the PDF is created and properly formatted
4. Check file size is reasonable (typically 5-50KB for simple documents)

Example validation workflow:
```python
import markdown
import weasyprint

# Test markdown content
md_content = """
# Test Document
- List item 1
- List item 2

**Bold text** and *italic text*

```python
print("Hello World")
```
"""

html = markdown.markdown(md_content, extensions=['fenced_code'])
full_html = f'<html><head><style>body{{font-family: Arial; margin: 40px;}}</style></head><body>{html}</body></html>'
weasyprint.HTML(string=full_html).write_pdf('test_output.pdf')
```

This validation takes 1-2 seconds and should always create a valid PDF file.

## Validation

- ALWAYS run through at least one complete end-to-end scenario after making changes.
- Always test with various markdown features: headers, lists, code blocks, tables, bold/italic text.
- Always run `black .` and `flake8 .` before committing or the linting will fail.
- PDF conversion typically takes 1-2 seconds for simple documents, up to 10 seconds for complex documents with many images or formatting.

## Common Tasks

The following are outputs from frequently run commands. Reference them instead of viewing, searching, or running bash commands to save time.

### Repository Structure
```
.
├── README.md
├── LICENSE  
└── .github/
    └── copilot-instructions.md
```

### Python Environment Check
```bash
python3 --version
# Python 3.12.3

pip --version  
# pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

### Required Libraries
The following libraries are essential for this project:
- `markdown`: Core markdown parsing (install time: 5 seconds)
- `weasyprint`: HTML to PDF conversion (install time: 15 seconds) 
- `reportlab`: Alternative PDF generation (install time: 8 seconds)
- `pdfkit`: Wrapper for wkhtmltopdf (install time: 2 seconds)
- `pytest`: Testing framework (install time: 5 seconds)
- `black`: Code formatter (install time: 8 seconds)
- `flake8`: Linter (install time: 5 seconds)

### Timing Expectations
- Library installation: 30-45 seconds total. NEVER CANCEL. Set timeout to 90+ seconds.
- PDF conversion: 1-2 seconds for simple documents, up to 10 seconds for complex ones.
- Code formatting (black): Less than 1 second for small files, up to 3 seconds for large codebases.
- Linting (flake8): Less than 1 second for small files, up to 5 seconds for large codebases.
- Test execution: 2-3 seconds for basic tests. NEVER CANCEL. Set timeout to 60+ seconds for comprehensive test suites.

### Common Error Solutions

**ImportError for markdown/weasyprint libraries:**
- Run: `pip install --user markdown weasyprint`
- Verification: `python3 -c "import markdown, weasyprint; print('Success')"`

**PDF generation fails:**
- Check markdown syntax is valid
- Ensure output directory is writable
- Verify HTML intermediate step works: `markdown.markdown(content)`

**Black formatting conflicts:**
- Run `black .` to auto-format all Python files
- Common issues: missing blank lines, string quote consistency

**Flake8 linting errors:**
- Line too long (E501): Break lines or use black formatter
- Unused imports (F401): Remove unused import statements  
- Missing blank lines (E302): Add proper spacing between functions/classes

## Key Project Features

This is a Python utility focused on:
- Converting GitHub-flavored markdown to PDF
- Preserving formatting including code blocks, tables, and styling
- Handling various markdown extensions (fenced_code, tables, etc.)
- Providing clean, professional PDF output

## Development Notes

- Always test with real markdown files, not just simple strings
- PDF output quality depends on CSS styling in HTML intermediate step
- WeasyPrint is preferred over alternatives for better rendering quality
- Consider file size optimization for large documents
- Test edge cases: special characters, code blocks, nested lists, tables