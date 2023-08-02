#!/usr/bin/python3
"""A program to convert a markdown file into an html file"""

import sys


def convert_md_html(md_file, html_file):
    """Convert a markdown file into a html file"""
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
    in_ul_list = False
    in_ol_list = False
    in_p_tag = False
    in_emb_tag = False
    in_b_tag = False

    for line in lines:
        i = 0
        cp_line = ""

        while i < len(line):
            # if part of string is '__':
            if line[i:i+2] == "__":
                # if we're not in an <em> tag
                if not in_emb_tag:
                    # open it and check for
                    cp_line += (f"<em>")
                    in_emb_tag = True
                else:
                    # else, close it and check
                    cp_line += (f"</em>")
                    in_emb_tag == False
                # pass the 2 characters
                i += 2


            elif line[i:i+2] == "**":
                if not in_b_tag:
                    cp_line += (f"<b>")
                    in_b_tag = True
                else:
                    cp_line += (f"</b>")
                    in_b_tag = False
                i += 2
            # next character in the loop
            else:
                cp_line += line[i]
                i += 1

        line = cp_line

        # adds titles
        if line.startswith("#"):
            # Count the number of hashtags in a line
            num_hashtag = line.count('#')
            # determine the level of <h> tag, 6 is the number max of levels
            level = min(num_hashtag, 6)
            # deletes the '#' and strip deletes the space
            level_txt = line[num_hashtag:].strip()
            # add the result to html content
            html_content += (f"<h{level}>{level_txt}</h{level}>\n")

        # adds ul lists
        elif line.startswith("- "):
            ul_text = line[1:].strip()
            # Checks if not in a list
            if not in_ul_list:
                # if not yet in a list, add <ul> tag
                html_content += "<ul>\n"
                # Now in list
                in_ul_list = True
            html_content += (f"\t<li>{ul_text}</li>\n")

        # adds ol lists
        elif line.startswith("* "):
            ol_text = line[1:].strip()
            # Checks if not in a list
            if not in_ol_list:
                # if not yet in a list, add <ol> tag
                html_content += "<ol>\n"
                # Now in list
                in_ol_list = True
            html_content += (f"\t<li>{ol_text}</li>\n")

        # elif p tag not open, add a p tag and check it
        elif not in_p_tag and line:
            # if no p tag, print first tag
            html_content += (f"<p>\n")
            # check inside p tag
            in_p_tag = True
            html_content += (f"\t{line}\n")

        # If p tag is open, add line
        elif in_p_tag is True and line:
            html_content += (f"\t\t<br \\>\n")
            html_content += (f"\t{line}\n")


        else:
            # otherwise if in a ul list but no "-"
            if in_ul_list:
                # close the ul tag
                html_content += (f"</ul>\n")
                # check not in ul list
                in_ul_list = False
            # elif in an ol list but no "*"
            elif in_ol_list:
                # close the ol tag
                html_content += (f"</ol>\n")
                # check not in ol list
                in_ol_list = False
            # elif in p tag, to close the p tag
            elif in_p_tag:
                html_content += (f"</p>\n")
                in_p_tag = False


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
