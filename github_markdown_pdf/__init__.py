"""
GitHub Markdown PDF - Convert GitHub Markdown to PDF.

A Python package for converting GitHub flavored Markdown files to properly formatted PDFs.
"""

__version__ = "0.1.0"
__author__ = "dhruv kejriwal"
__email__ = ""
__description__ = "Get proper formatted PDF using Python without any problem"

from .converter import MarkdownToPDFConverter
from .exceptions import MarkdownPDFError, ConversionError, FileNotFoundError

__all__ = [
    "MarkdownToPDFConverter",
    "MarkdownPDFError",
    "ConversionError", 
    "FileNotFoundError",
]