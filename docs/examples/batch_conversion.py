"""
Example of batch converting multiple markdown files.
"""

import os
from github_markdown_pdf import MarkdownToPDFConverter

# Create converter instance
converter = MarkdownToPDFConverter()

# Define input and output directories
input_dir = 'markdown_files'
output_dir = 'pdf_files'

# Create directories if they don't exist
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Batch convert all markdown files
try:
    results = converter.batch_convert(input_dir, output_dir)
    
    print(f"Batch conversion results:")
    for input_file, output_file in results.items():
        if output_file.startswith('Error:'):
            print(f"❌ {input_file}: {output_file}")
        else:
            print(f"✅ {input_file} -> {output_file}")
            
except Exception as e:
    print(f"Error during batch conversion: {e}")