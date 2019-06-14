#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys


def fetch_db_data(db, command):
    """
    Send queries to the sqlite database and return the results.
    :param db: The path to the database.
    :param command: The Sqlite command.
    :return:
    """
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(command)
        return cur.fetchall()
    except Exception as e:
        sys.exit("Error reading the database: %s" % e)


def create_db_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Exception as e:
        sys.exit("Error reading the database: %s" % e)
