#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
common.py
Python 3.8+
Author: niftycode
Date created: June 14th, 2020
Date modified: October 27th, 2020
"""


import sqlite3
import sys
import enum
import platform


class Platform(enum.Enum):
    OTHER = 0
    LINUX = 1
    MAC = 2
    WINDOWS = 3


def get_platform():
    system = platform.system()
    if system == 'Linux':
        return Platform.LINUX
    if system == 'Darwin':
        return Platform.MAC
    if system == 'Windows':
        return Platform.WINDOWS
    raise NotImplementedError(f"Platform {system} is not supported yet!")


def fetch_db_data(db, command) -> list:
    """
    Send queries to the sqlite database and return the results.
    :param db: The path to the database.
    :param command: The Sqlite command.
    :return: Data from the database
    """
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(command)
        return cur.fetchall()
    except Exception as e:
        sys.exit("Error reading the database: %s" % e)
