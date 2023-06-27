#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cli.py
Entrypoint to the command line interface.
Python 3.9+
Date created: October 15th, 2020
Date modified: June 2nd, 2023
"""

import argparse
import os
import sys

from os.path import expanduser

from imessage_reader import fetch_data
from imessage_reader import info


# Path to the chat.db file on macOS
# Note: This path is used if the user does not specify a path.
MACOS_DB_PATH = expanduser("~") + "/Library/Messages/chat.db"


def get_parser() -> argparse.ArgumentParser:
    """Create the argument parser

    :rtype: object
    """
    parser = argparse.ArgumentParser(
        description="A tool to fetch messages from the chat.db file."
    )

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        nargs="?",
        const=MACOS_DB_PATH,
        default=MACOS_DB_PATH,
        help="Path to the database file"
    )

    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        default="nothing",
        help="Specify the output: e => Excel, s => SQLite"
    )

    parser.add_argument(
        "-r",
        "--recipients",
        help="Show the recipients",
        action="store_true"
    )

    parser.add_argument(
        "-v",
        "--version",
        help="Show the current version.",
        action="store_true"
    )

    return parser


def check_database_path(args):
    """ Parse arguments from sys.argv and invoke the evaluate method.

    :param args: the user's input
    """
    if args.path == MACOS_DB_PATH:
        evaluate(MACOS_DB_PATH, args.output, args.recipients, args.version)
    elif os.path.isdir(args.path):
        db_path = args.path + "/chat.db"
        evaluate(db_path, args.output, args.recipients, args.version)
    else:
        sys.exit("Path doesn't exist! Exit program.")


def evaluate(path: str, output: str, recipients: bool, version: bool):
    """Evaluate the given options and perform the appropriate actions.

    :param path: path to the chat.db file
    :param output: create an Excel/SQLite3 file
    :param recipients: recipients of the messages
    :param version: specify if the version of this program should be shown
    """
    data = fetch_data.FetchData(path)

    if version:
        info.app_info()
        sys.exit()

    if recipients:
        data.show_user_txt("recipients")
        sys.exit()

    if output == "e" or output == "excel":
        data.show_user_txt("excel")
    elif output == "s" or output == "sqlite" or output == "sqlite3":
        data.show_user_txt("sqlite")
    else:
        data.show_user_txt("nothing")


def main():
    """Entrypoint to the command-line interface (CLI).
    """
    parser = get_parser()
    args = parser.parse_args()
    check_database_path(args)


if __name__ == "__main__":
    main()
