#!/usr/bin/python3
"""A program to convert a markdown file into an html file"""

import sys


def convert_md_html(md_file, html_file):
    """Convert a markdown file into an html file"""
    try:
        # Open the md file, read and store content in the variable md_content
        with open(md_file, 'r') as md:
            md_content = md.read()

    # If md_file does not exist, display an error message
    except FileNotFoundError:
        sys.stderr.write(f"Missing {md_file}\n")
        exit(1)

    # Separate each line of md_content
    lines = md_content.split('\n')

    # create html_content variable
    html_content = ""

    for line in lines:
        if line.startswith("#"):
            # Count the number of hashtags in a line
            num_hashtag = line.count('#')
            # determine the level of <h> tag, 6 is the number max of levels
            level = min(num_hashtag, 6)
            # deletes the '#' and strip deletes the space
            level_txt = line[num_hashtag:].strip()
            # add the result to html content
            html_content += (f"<h{level}>{level_txt}</h{level}>\n")

    # Open the output file in html
    with open(html_file, 'w') as html:
        # Write the converted HTML content into the file
        html.write(html_content)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    else:
        # Assign arguments to the variables
        md_file = sys.argv[1]
        html_file = sys.argv[2]

    # Use the method
    convert_md_html(md_file, html_file)
    exit(0)
