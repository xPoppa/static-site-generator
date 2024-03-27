import os
import shutil
import argparse
from typing import Any

parser = argparse.ArgumentParser()

#-db DATABASE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-f", "--froms", help="Choose to directory to copy files from")
parser.add_argument("-t", "--to", help="Choose directory to copy files to\n will create directory if it doesn't exist yet")

args = parser.parse_args()


def copy_static_to_public():
    if os.path.exists(args.to):
        shutil.rmtree(args.to)
    print(f"the from path: {args.froms} does it exist?: {os.path.exists(args.froms)}")
    print(f"the to path: {args.to} does it exist?: {os.path.exists(args.to)}")
    print(f"list dir outcome {os.listdir(args.froms)}")
    if not os.path.exists(args.to):
        os.mkdir(args.to)
    items = os.listdir(args.froms)
    recurse(items)

def recurse(items: list[Any]) -> None:
    print(items)
    if len(items) == 0:
        #shutil.r mtree(args.froms)
        return
    first_item = items[0]
    if os.path.isfile(os.path.join(args.froms, first_item)):
        shutil.copy(os.path.join(args.froms, first_item), args.to)
        return recurse(items[1:])
    if os.path.isdir(os.path.join(args.froms, first_item)):
        nested_items = os.listdir(os.path.join(args.froms, first_item))
        for idx, ni in enumerate(nested_items):
            nested_items[idx] = os.path.join(first_item, ni)
        items.extend(nested_items)
        return recurse(items[1:])
        
        
copy_static_to_public()
