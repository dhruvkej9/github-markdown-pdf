"""
Utility functions for GitHub Markdown PDF package.
"""

import os
import re
from pathlib import Path
from typing import Optional, Dict, Any


def validate_markdown_file(file_path: str) -> bool:
    """
    Validate if the given file path is a valid markdown file.
    
    Args:
        file_path (str): Path to the markdown file
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not os.path.exists(file_path):
        return False
    
    path = Path(file_path)
    return path.suffix.lower() in ['.md', '.markdown']


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to be safe for filesystem operations.
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Sanitized filename
    """
    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Remove leading/trailing whitespace and dots
    sanitized = sanitized.strip(' .')
    
    # Ensure filename is not empty
    if not sanitized:
        sanitized = 'output'
        
    return sanitized


def get_output_path(input_path: str, output_dir: Optional[str] = None) -> str:
    """
    Generate output PDF path based on input markdown file path.
    
    Args:
        input_path (str): Path to input markdown file
        output_dir (str, optional): Output directory. Defaults to same as input.
        
    Returns:
        str: Output PDF file path
    """
    input_file = Path(input_path)
    pdf_filename = sanitize_filename(input_file.stem) + '.pdf'
    
    if output_dir:
        return os.path.join(output_dir, pdf_filename)
    else:
        return os.path.join(input_file.parent, pdf_filename)


def ensure_directory_exists(directory: str) -> None:
    """
    Ensure that a directory exists, create if it doesn't.
    
    Args:
        directory (str): Directory path to ensure exists
    """
    os.makedirs(directory, exist_ok=True)


def get_default_css() -> str:
    """
    Get default CSS styling for PDF generation.
    
    Returns:
        str: CSS styling string
    """
    return """
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: #24292e;
        max-width: 980px;
        margin: 0 auto;
        padding: 45px;
    }
    
    h1, h2, h3, h4, h5, h6 {
        margin-top: 24px;
        margin-bottom: 16px;
        font-weight: 600;
        line-height: 1.25;
    }
    
    h1 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h2 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    
    code {
        background-color: rgba(27,31,35,0.05);
        border-radius: 3px;
        font-size: 85%;
        margin: 0;
        padding: 0.2em 0.4em;
    }
    
    pre {
        background-color: #f6f8fa;
        border-radius: 6px;
        font-size: 85%;
        line-height: 1.45;
        overflow: auto;
        padding: 16px;
    }
    
    blockquote {
        border-left: 0.25em solid #dfe2e5;
        color: #6a737d;
        padding: 0 1em;
        margin: 0;
    }
    
    table {
        border-collapse: collapse;
        border-spacing: 0;
        width: 100%;
    }
    
    table th, table td {
        border: 1px solid #dfe2e5;
        padding: 6px 13px;
    }
    
    table tr:nth-child(2n) {
        background-color: #f6f8fa;
    }
    """