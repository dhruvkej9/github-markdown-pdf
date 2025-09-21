"""
Example of using custom CSS styling.
"""

from github_markdown_pdf import MarkdownToPDFConverter

# Custom CSS for styling the PDF
custom_css = """
/* Custom styling for PDF output */
body {
    font-family: 'Georgia', serif;
    font-size: 14px;
    line-height: 1.8;
    color: #2c3e50;
    margin: 40px;
}

h1 {
    color: #e74c3c;
    border-bottom: 3px solid #e74c3c;
    padding-bottom: 10px;
}

h2 {
    color: #3498db;
    border-bottom: 2px solid #3498db;
    padding-bottom: 5px;
}

code {
    background-color: #f8f9fa;
    color: #e83e8c;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
}

pre {
    background-color: #2d3748;
    color: #e2e8f0;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
}

blockquote {
    border-left: 4px solid #f39c12;
    background-color: #fef9e7;
    padding: 10px 20px;
    margin: 20px 0;
    font-style: italic;
}

table {
    border: 2px solid #34495e;
    border-radius: 8px;
}

table th {
    background-color: #34495e;
    color: white;
    padding: 12px;
    text-align: left;
}

table td {
    padding: 10px;
    border-bottom: 1px solid #bdc3c7;
}
"""

# Create converter with custom CSS
converter = MarkdownToPDFConverter(custom_css=custom_css)

# Convert markdown file with custom styling
input_file = 'styled_example.md'
output_file = 'styled_example.pdf'

try:
    result_path = converter.convert(input_file, output_file)
    print(f"Successfully converted {input_file} to {result_path} with custom styling")
except Exception as e:
    print(f"Error converting file: {e}")