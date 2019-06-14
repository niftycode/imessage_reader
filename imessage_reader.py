#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
imessage_reader.py
The main file with the entry point for this program.
Python 3.7
Author: niftycode
Date created: 14.06.2019
"""


import os
from imessage_reader import common

VERSION = '1.0.0'

# The path to the imessage database
DB_PATH = '/Users/{0}/Library/Messages/chat.db'.format(os.getlogin())


# TODO: Move class to separate file.
class Recipient:
    def __init__(self, rowid, phone_id):
        self.rowid = rowid
        self.phone_id = phone_id

    def __repr__(self):
        return f"{self.rowid}: {self.id}"


def fetch_recipients():
    sql_command = "SELECT ROWID, id from handle"
    rval = common.fetch_db_data(DB_PATH, sql_command)

    print(rval)


"""
def new_db_connection():
    recipients = []
    handle_data = common.fetch_db_data(DB_PATH, "SELECT * FROM handle")
    print(handle_data)
    '''
    for h in handle_data:
        recipients.append(Recipient(row[0], row[1]))
        print(recipients)
    '''


new_db_connection()
"""


def main():
    """
    The entry point of this program.
    """
    fetch_recipients()


if __name__ == '__main__':
    print('\n\n    ##### A Python script to read iMessage data #####')
    print('    #               Created by niftycode            #')
    print(f'    #                  Version {VERSION}                #')
    print('    #################################################\n\n')
    print()
    main()
