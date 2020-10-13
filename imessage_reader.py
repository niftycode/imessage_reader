#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
imessage_reader.py
The main file with the entry point for this program.
Python 3.8+
Author: niftycode
Date created: June 14th, 2020
Date modified: October 13th, 2020
"""

import argparse
import sys
from src import info
from src import fetch_data


def get_parser():
    parser = argparse.ArgumentParser(description="A tool to fetch imessages "
                                                 "from the chat.db (macOS).")

    parser.add_argument('-e', '--excel',
                        help='Create Excel file containing user id and messages.',
                        action='store_true')

    parser.add_argument('-v', '--version',
                        help='Show the current version.',
                        action='store_true')

    args = parser.parse_args()
    return args


def evaluate(args):
    """
    It parses arguments from sys.argv and performs the appropriate actions.
    :param args: The user's input
    """
    data = fetch_data.FetchData()
    if args.version:
        info.app_info()
    elif args.excel:
        data.show_user_txt(True)
    else:
        data.show_user_txt(False)


def main():
    """
    Entrypoint to the command-line interface (CLI).
    """

    args = get_parser()
    sys.stdout.write(str(evaluate(args)))


if __name__ == '__main__':
    main()
