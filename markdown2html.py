#!/usr/bin/python3
"""A program to convert a markdown file to an html file"""

import sys
import os

def convert_md_html(md_file, html_file):
    """Convert a markdown file to an html file"""
    try:
        # Open the md file, read its content, and store it in the variable md_content
        with open(md_file, 'r') as md:
            md_content = md.read()

        # Open the output file in html
        with open(html_file, 'w') as html:
            # Write the converted content to the html file
            html.write(md_content)

        print(f"Conversion successful. HTML file created: {html_file}")

    except FileNotFoundError:
        # If md_file does not exist, display an error message on STDERR
        sys.stderr.write(f"Missing {md_file}\n")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        # If the number of arguments is less than 3, display usage information on STDERR
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    else:
        # Assign arguments to the variables
        md_file = sys.argv[1]
        html_file = sys.argv[2]

    # Use the function to convert markdown to html
    convert_md_html(md_file, html_file)
    exit(0)
