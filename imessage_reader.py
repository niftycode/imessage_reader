#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
imessage_reader.py
The main file with the entry point for this program.
Python 3.9+
Author: niftycode
Date created: June 14th, 2020
Date modified: October 8th, 2020
"""


from src import info
from src import fetch_data


def main():
    """
    The entry point of this program.
    """

    m = fetch_data.FetchData()
    m.fetch_user_txt(True)  # -> True: Export data (Excel file)


if __name__ == '__main__':
    # TODO: Add CLI
    info.app_info()
    main()
