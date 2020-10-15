#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
common.py
Python 3.8+
Author: niftycode
Date created: June 14th, 2020
Date modified: October 1st, 2020
"""


import sqlite3
import sys


def fetch_db_data(db, command):
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
