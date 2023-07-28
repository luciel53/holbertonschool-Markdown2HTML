#!/usr/bin/python3
"""
A program to convert a markdown file to an html file
"""

from sys import argv, exit

def convert_md_html(md_file, html_file):
    """Convert a markdown file to a html file"""
    try:
        # Open the md file, read it and stock it in the variable md_content
        with open(md_file, 'r') as md:
            md_content = md.read()

    # if md_file does not exist, message error
    except FileNotFoundError:
        print("Missing <filename>")
        exit(1)

    # Open the output file in html
    with open(html_file, 'w') as html:
        # You can implement the conversion logic from Markdown to HTML here.
        # For this example, I'll just write a simple HTML content.
        html.write("")

if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    else:
        # Give arguments to the variables
        md_file = argv[1]
        html_file = argv[2]

    # Use the function to convert Markdown to HTML
    convert_md_html(md_file, html_file)
    exit(0)

