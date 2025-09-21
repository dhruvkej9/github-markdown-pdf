"""
Main converter class for GitHub Markdown to PDF conversion.
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path

from .exceptions import ConversionError, FileNotFoundError, InvalidFormatError
from .utils import validate_markdown_file, get_output_path, ensure_directory_exists, get_default_css


class MarkdownToPDFConverter:
    """
    Main class for converting GitHub flavored Markdown to PDF.
    """
    
    def __init__(self, css_path: Optional[str] = None, custom_css: Optional[str] = None):
        """
        Initialize the converter.
        
        Args:
            css_path (str, optional): Path to custom CSS file
            custom_css (str, optional): Custom CSS string
        """
        self.css_path = css_path
        self.custom_css = custom_css
        self.default_css = get_default_css()
        
    def convert(self, 
                markdown_path: str, 
                output_path: Optional[str] = None,
                **options) -> str:
        """
        Convert markdown file to PDF.
        
        Args:
            markdown_path (str): Path to input markdown file
            output_path (str, optional): Path for output PDF file
            **options: Additional conversion options
            
        Returns:
            str: Path to generated PDF file
            
        Raises:
            FileNotFoundError: If markdown file doesn't exist
            InvalidFormatError: If file is not a valid markdown file
            ConversionError: If conversion fails
        """
        # Validate input file
        if not os.path.exists(markdown_path):
            raise FileNotFoundError(f"Markdown file not found: {markdown_path}")
            
        if not validate_markdown_file(markdown_path):
            raise InvalidFormatError(f"Invalid markdown file: {markdown_path}")
            
        # Determine output path
        if output_path is None:
            output_path = get_output_path(markdown_path)
        
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir:
            ensure_directory_exists(output_dir)
            
        try:
            # Read markdown content
            with open(markdown_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
                
            # Convert markdown to HTML (placeholder - will need actual implementation)
            html_content = self._markdown_to_html(markdown_content)
            
            # Apply CSS styling
            styled_html = self._apply_css_styling(html_content)
            
            # Convert HTML to PDF (placeholder - will need actual implementation)
            self._html_to_pdf(styled_html, output_path)
            
            return output_path
            
        except Exception as e:
            raise ConversionError(f"Failed to convert {markdown_path} to PDF: {str(e)}")
    
    def _markdown_to_html(self, markdown_content: str) -> str:
        """
        Convert markdown content to HTML.
        
        Args:
            markdown_content (str): Markdown content string
            
        Returns:
            str: HTML content string
        """
        # Placeholder implementation
        # In a real implementation, you would use libraries like:
        # - markdown
        # - mistune
        # - markdown2
        # - commonmark
        
        # For now, just wrap in basic HTML structure
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Converted Markdown</title>
        </head>
        <body>
            <pre>{markdown_content}</pre>
        </body>
        </html>
        """
        return html
    
    def _apply_css_styling(self, html_content: str) -> str:
        """
        Apply CSS styling to HTML content.
        
        Args:
            html_content (str): HTML content string
            
        Returns:
            str: HTML content with CSS styling applied
        """
        css_content = self.default_css
        
        # Add custom CSS if provided
        if self.custom_css:
            css_content += "\n" + self.custom_css
            
        # Load CSS from file if provided
        if self.css_path and os.path.exists(self.css_path):
            with open(self.css_path, 'r', encoding='utf-8') as f:
                css_content += "\n" + f.read()
        
        # Insert CSS into HTML
        styled_html = html_content.replace(
            '</head>',
            f'<style>{css_content}</style>\n</head>'
        )
        
        return styled_html
    
    def _html_to_pdf(self, html_content: str, output_path: str) -> None:
        """
        Convert HTML content to PDF file.
        
        Args:
            html_content (str): HTML content string
            output_path (str): Output PDF file path
        """
        # Placeholder implementation
        # In a real implementation, you would use libraries like:
        # - weasyprint
        # - pdfkit
        # - reportlab
        # - playwright
        
        # For now, just create a simple text file as proof of concept
        with open(output_path.replace('.pdf', '.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        # Create a dummy PDF file
        with open(output_path, 'wb') as f:
            f.write(b'%PDF-1.4\n%Placeholder PDF file\n')
    
    def batch_convert(self, 
                     input_dir: str, 
                     output_dir: Optional[str] = None,
                     pattern: str = "*.md") -> Dict[str, str]:
        """
        Convert multiple markdown files to PDF.
        
        Args:
            input_dir (str): Directory containing markdown files
            output_dir (str, optional): Output directory for PDF files
            pattern (str): File pattern to match. Defaults to "*.md"
            
        Returns:
            Dict[str, str]: Dictionary mapping input files to output files
        """
        input_path = Path(input_dir)
        if not input_path.exists():
            raise FileNotFoundError(f"Input directory not found: {input_dir}")
            
        results = {}
        markdown_files = input_path.glob(pattern)
        
        for md_file in markdown_files:
            try:
                if output_dir:
                    output_file = os.path.join(output_dir, md_file.stem + '.pdf')
                else:
                    output_file = None
                    
                converted_path = self.convert(str(md_file), output_file)
                results[str(md_file)] = converted_path
                
            except Exception as e:
                results[str(md_file)] = f"Error: {str(e)}"
                
        return results