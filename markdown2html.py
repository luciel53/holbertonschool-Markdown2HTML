#!/usr/bin/python3
"""
Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name

R   equirements:

    If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
    If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
    Otherwise, print nothing and exit 0
"""


from sys import argv as arg


def convert_md_html(md_file, html_file):
    """ Convert a markdown file in a html file"""

    try:
        # Open the md file, read it and stock it in the variable md_content
        with open(md_file, 'r') as md:
            md_content = md.read()

    # if md_file does not exist, message error
    except FileNotFoundError:
        print("Missing <filename>")
        exit (1)

    # Open the output file in html
    with open(html_file, 'w') as html:
        html.write("")



if __name__ == "__main__":

    # if number of arguments is < 3, print an error
    if len(arg) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit (1)

    else:
        #else, give arguments to the variables
        md_file = arg[1]
        html_file = arg[2]

#Use the method
convert_md_html(md_file, html_file)
exit(0)
