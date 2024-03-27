from copy_static import copy_files_recursive
from extract_markdown import generate_page, generate_page_recursive
import argparse

parser = argparse.ArgumentParser()

#-db DATABASE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-f", "--froms", help="Choose to directory to copy files from")
parser.add_argument("-t", "--to", help="Choose directory to copy files to\n will create directory if it doesn't exist yet")

args = parser.parse_args()

generate_page_recursive("content", "template.html", "public")

copy_files_recursive(args.froms, args.to)

