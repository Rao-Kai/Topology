#!/usr/bin/env python
import argparse
import pathlib

import colorama

from arc_utilities.conversions import parse_file_size
from arc_utilities.filesystem_utils import directory_size, ask_to_remove_directories


def main():
    colorama.init(autoreset=True)
    parser = argparse.ArgumentParser("finds directories smaller than a given size, asks for confirmation, then deletes")
    parser.add_argument('root', type=pathlib.Path, help="root directory", nargs='+')
    parser.add_argument('size', type=str, help="size, like 10k, 20mb, etc. ")

    args = parser.parse_args()

    size_threshold_bytes = parse_file_size(args.size)

    directories_to_remove = []
    for root in args.root:
        for d in root.iterdir():
            if d.is_dir():
                size_bytes = directory_size(d)
                if size_bytes < size_threshold_bytes:
                    directories_to_remove.append(d)

    ask_to_remove_directories(directories_to_remove)


if __name__ == '__main__':
    main()
