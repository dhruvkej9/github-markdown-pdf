#!/usr/bin/env python3
"""
Command-line interface for GitHub Markdown PDF converter.

Usage:
    md2pdf input.md [output.pdf] [options]
    
Examples:
    md2pdf README.md
    md2pdf README.md custom_output.pdf
    md2pdf docs/ --batch --output-dir pdfs/
"""

import argparse
import sys
import os
from pathlib import Path

try:
    from github_markdown_pdf import MarkdownToPDFConverter
    from github_markdown_pdf.exceptions import MarkdownPDFError
except ImportError:
    # Handle case where package is not installed
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from github_markdown_pdf import MarkdownToPDFConverter
    from github_markdown_pdf.exceptions import MarkdownPDFError


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Convert GitHub flavored Markdown to PDF',
        epilog='Examples:\n'
               '  md2pdf README.md\n'
               '  md2pdf README.md output.pdf\n'
               '  md2pdf docs/ --batch --output-dir pdfs/',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'input',
        help='Input markdown file or directory (for batch mode)'
    )
    
    parser.add_argument(
        'output',
        nargs='?',
        help='Output PDF file (optional, defaults to input filename with .pdf extension)'
    )
    
    parser.add_argument(
        '--batch',
        action='store_true',
        help='Batch mode: convert all markdown files in input directory'
    )
    
    parser.add_argument(
        '--output-dir',
        help='Output directory for batch mode'
    )
    
    parser.add_argument(
        '--css',
        help='Path to custom CSS file for styling'
    )
    
    parser.add_argument(
        '--pattern',
        default='*.md',
        help='File pattern for batch mode (default: *.md)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not os.path.exists(args.input):
        print(f"Error: Input path '{args.input}' does not exist.", file=sys.stderr)
        return 1
    
    if args.batch and not os.path.isdir(args.input):
        print(f"Error: Batch mode requires input to be a directory.", file=sys.stderr)
        return 1
        
    if not args.batch and os.path.isdir(args.input):
        print(f"Error: Input is a directory. Use --batch flag for batch processing.", file=sys.stderr)
        return 1
    
    try:
        # Create converter instance
        converter = MarkdownToPDFConverter(css_path=args.css)
        
        if args.batch:
            # Batch processing mode
            if args.verbose:
                print(f"Starting batch conversion in directory: {args.input}")
                print(f"Pattern: {args.pattern}")
                if args.output_dir:
                    print(f"Output directory: {args.output_dir}")
            
            results = converter.batch_convert(
                input_dir=args.input,
                output_dir=args.output_dir,
                pattern=args.pattern
            )
            
            success_count = 0
            error_count = 0
            
            for input_file, output_result in results.items():
                if output_result.startswith('Error:'):
                    error_count += 1
                    if args.verbose:
                        print(f"❌ {input_file}: {output_result}")
                else:
                    success_count += 1
                    if args.verbose:
                        print(f"✅ {input_file} -> {output_result}")
            
            print(f"Batch conversion completed: {success_count} successful, {error_count} errors")
            
            if error_count > 0:
                return 1
                
        else:
            # Single file processing mode
            if args.verbose:
                print(f"Converting: {args.input}")
                if args.output:
                    print(f"Output: {args.output}")
            
            output_path = converter.convert(args.input, args.output)
            
            if args.verbose:
                print(f"✅ Successfully converted to: {output_path}")
            else:
                print(output_path)
    
    except MarkdownPDFError as e:
        print(f"Conversion error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())