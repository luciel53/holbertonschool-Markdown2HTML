#!/usr/bin/python3
"""A program to convert a markdown file in an html file"""


from sys import argv as arg


def convert_md_html(md_file, html_file):
    """Convert a markdown file in a html file"""

    try:

        with open(md_file, 'r') as md:
            md_content = md.read()

    except FileNotFoundError:
        print("Missing <filename>")
        exit (1)

    with open(html_file, 'w') as html:
        html.write("")



if __name__ == "__main__":
    """To not execute this script"""

    if len(arg) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit (1)

    else:
        md_file = arg[1]
        html_file = arg[2]

convert_md_html(md_file, html_file)
exit(0)
