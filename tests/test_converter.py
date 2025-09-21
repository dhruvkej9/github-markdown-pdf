"""
Tests for the MarkdownToPDFConverter class.
"""

import os
import tempfile
import unittest
from pathlib import Path

from github_markdown_pdf import MarkdownToPDFConverter
from github_markdown_pdf.exceptions import (
    ConversionError, 
    FileNotFoundError, 
    InvalidFormatError
)


class TestMarkdownToPDFConverter(unittest.TestCase):
    """Test cases for MarkdownToPDFConverter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.converter = MarkdownToPDFConverter()
        self.test_data_dir = Path(__file__).parent / 'test_data'
        self.temp_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Clean up test fixtures."""
        # Clean up temporary files
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_converter_initialization(self):
        """Test converter initialization."""
        converter = MarkdownToPDFConverter()
        self.assertIsNotNone(converter)
        self.assertIsNotNone(converter.default_css)
        
    def test_converter_with_custom_css(self):
        """Test converter initialization with custom CSS."""
        custom_css = "body { color: red; }"
        converter = MarkdownToPDFConverter(custom_css=custom_css)
        self.assertEqual(converter.custom_css, custom_css)
    
    def test_file_not_found_error(self):
        """Test FileNotFoundError when input file doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            self.converter.convert("nonexistent_file.md")
    
    def test_invalid_format_error(self):
        """Test InvalidFormatError for non-markdown files."""
        # Create a temporary non-markdown file
        temp_file = os.path.join(self.temp_dir, "test.txt")
        with open(temp_file, 'w') as f:
            f.write("This is not a markdown file")
            
        with self.assertRaises(InvalidFormatError):
            self.converter.convert(temp_file)
    
    def test_successful_conversion(self):
        """Test successful markdown to PDF conversion."""
        # Create a temporary markdown file
        temp_md_file = os.path.join(self.temp_dir, "test.md")
        with open(temp_md_file, 'w') as f:
            f.write("# Test Markdown\n\nThis is a test markdown file.")
            
        # Convert to PDF
        output_path = self.converter.convert(temp_md_file)
        
        # Check that output file was created
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(output_path.endswith('.pdf'))
    
    def test_batch_conversion(self):
        """Test batch conversion of multiple markdown files."""
        # Create multiple test markdown files
        test_files = ['test1.md', 'test2.md', 'test3.md']
        for filename in test_files:
            filepath = os.path.join(self.temp_dir, filename)
            with open(filepath, 'w') as f:
                f.write(f"# {filename}\n\nContent for {filename}")
        
        # Perform batch conversion
        results = self.converter.batch_convert(self.temp_dir)
        
        # Check results
        self.assertEqual(len(results), len(test_files))
        for input_file, output_file in results.items():
            self.assertTrue(os.path.exists(input_file))
            if not output_file.startswith('Error:'):
                self.assertTrue(os.path.exists(output_file))
    
    def test_output_path_generation(self):
        """Test output path generation."""
        # Create a temporary markdown file
        temp_md_file = os.path.join(self.temp_dir, "test_output.md")
        with open(temp_md_file, 'w') as f:
            f.write("# Test\n\nTest content.")
            
        # Convert with default output path
        output_path = self.converter.convert(temp_md_file)
        expected_output = os.path.join(self.temp_dir, "test_output.pdf")
        self.assertEqual(output_path, expected_output)
        
    def test_custom_output_path(self):
        """Test conversion with custom output path."""
        # Create a temporary markdown file
        temp_md_file = os.path.join(self.temp_dir, "test_custom.md")
        with open(temp_md_file, 'w') as f:
            f.write("# Test Custom\n\nTest content.")
            
        # Convert with custom output path
        custom_output = os.path.join(self.temp_dir, "custom_name.pdf")
        output_path = self.converter.convert(temp_md_file, custom_output)
        
        self.assertEqual(output_path, custom_output)
        self.assertTrue(os.path.exists(custom_output))


if __name__ == '__main__':
    unittest.main()