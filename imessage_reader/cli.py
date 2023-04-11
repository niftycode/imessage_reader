#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cli.py
Entrypoint to the command line interface.
Python 3.8+
Date created: October 15th, 2020
Date modified: April 9th, 2023
"""

import argparse

from imessage_reader import fetch_data
from imessage_reader import info


def get_parser() -> argparse.ArgumentParser:
    """Create the argument parser

    Returns:
        argparse.ArgumentParser: parser
    """
    parser = argparse.ArgumentParser(
        description="A tool to fetch imessages from the chat.db (macOS)."
    )

    parser.add_argument(
        "-f", "--file", type=str, required=False, help="Path to the chat.db file."
    )

    parser.add_argument(
        "-e",
        "--excel",
        help="Create Excel file containing user id and messages.",
        action="store_true",
    )

    parser.add_argument(
        "-s", "--sqlite", help="Create a SQLite3 database", action="store_true"
    )

    parser.add_argument(
        "-r", "--recipients", help="Show the recipients", action="store_true"
    )

    parser.add_argument(
        "-v", "--version", help="Show the current version.", action="store_true"
    )

    return parser


def evaluate(args):
    """
    Parse arguments from sys.argv and perform the appropriate actions.
    :param args: The user's input
    """
    data = fetch_data.FetchData()
    if args.version:
        info.app_info()
    elif args.file:
        fetch_data.print_path(args.file)
    elif args.excel:
        data.show_user_txt("excel")
    elif args.sqlite:
        data.show_user_txt("sqlite")
    elif args.recipients:
        data.show_user_txt("recipients")
    else:
        data.show_user_txt("nothing")


def main():
    """
    Entrypoint to the command-line interface (CLI).
    """
    parser = get_parser()
    args = parser.parse_args()
    evaluate(args)


if __name__ == "__main__":
    main()
