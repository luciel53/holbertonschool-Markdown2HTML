#!/usr/bin/python3
"""A program to convert a markdown file in an html file"""


from sys import argv as arg


def convert_md_html(md_file, html_file):
    """Convert a markdown file in a html file"""
    try:
        # Open the md file, read it and stock it in the variable md_content
        with open(md_file, 'r') as md:
            md_content = md.read()

    # if md_file does not exist, message error
    except FileNotFoundError:
        print(f"Missing {md_file}")
        exit(1)

    print("Missing README.md")
    exit(1)


if __name__ == "__main__":
    if len(arg) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    else:
        # Give arguments to the variables
        md_file = arg[1]
        html_file = arg[2]

    # Use the method
    convert_md_html(md_file, html_file)
    exit(0)
