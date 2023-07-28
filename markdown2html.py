#!/usr/bin/python3
"""A program to convert a markdown file in an html file"""


import sys


def convert_md_html(md_file, html_file):
    """Convert a markdown file in a html file"""
    try:
        # Open the md file, read it and stock it in the variable md_content
        with open(md_file, 'r') as md:
            md_content = md.read()

    # if md_file does not exist, message error
    except FileNotFoundError:
        sys.stderr.write(f"Missing {md_file}\n")
        exit(1)

    # Open the output file in html
    with open(html_file, 'w') as html:
        # Write "" in document
        html.write("")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    else:
        # Give arguments to the variables
        md_file = sys.argv[1]
        html_file = sys.argv[2]

    # Use the method
    convert_md_html(md_file, html_file)
    exit(0)
