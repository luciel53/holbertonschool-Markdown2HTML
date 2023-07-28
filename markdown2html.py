#!/usr/bin/python3
"""A program to convert a markdown file in an html file"""
from sys import argv


if __name__ == "__main__":
    """mod"""
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    else:
        # Give argvuments to the variables
        md_file = argv[1]
        html_file = argv[2]


def convert_md_html(md_file, html_file):
    """Convert a markdown file in a html file"""
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
        html.write("")


convert_md_html(md_file, html_file)
exit(0)
