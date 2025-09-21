"""
Custom exceptions for GitHub Markdown PDF package.
"""


class MarkdownPDFError(Exception):
    """Base exception class for all markdown to PDF conversion errors."""
    pass


class ConversionError(MarkdownPDFError):
    """Exception raised when markdown to PDF conversion fails."""
    pass


class FileNotFoundError(MarkdownPDFError):
    """Exception raised when input markdown file is not found."""
    pass


class InvalidFormatError(MarkdownPDFError):
    """Exception raised when input file format is invalid."""
    pass


class ConfigurationError(MarkdownPDFError):
    """Exception raised when there are configuration issues."""
    pass