"""
Basic example of using GitHub Markdown PDF converter.
"""

from github_markdown_pdf import MarkdownToPDFConverter

# Create converter instance
converter = MarkdownToPDFConverter()

# Convert a markdown file to PDF
input_file = 'example.md'
output_file = 'example.pdf'

try:
    result_path = converter.convert(input_file, output_file)
    print(f"Successfully converted {input_file} to {result_path}")
except Exception as e:
    print(f"Error converting file: {e}")