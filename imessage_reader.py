#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
imessage_reader.py
The main file with the entry point for this program.
Python 3.7
Author: niftycode
Date created: 14.06.2019
"""


from os.path import expanduser
from imessage_reader import common

VERSION = '1.0.1'

# The path to the iMessage database
# DB_PATH = '/Users/{0}/Library/Messages/chat.db'.format(os.getlogin())
DB_PATH = expanduser("~") + '/Desktop/chat.db'  # for testing only


# TODO: Move class to separate file.
class MessageData:
    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text

    def __repr__(self):
        return f"{self.user_id}: {self.text}\n\n"


"""
class Recipient:
    def __init__(self, rowid, phone_id):
        self.rowid = rowid
        self.phone_id = phone_id

    def __repr__(self):
        return f"{self.rowid}: {self.phone_id}"


class Messages:
    def __init__(self, message, handle_id):
        self.message = message
        self.handle_id = handle_id

    def __repr__(self):
        return f"{self.handle_id}: {self.message}"
"""


def fetch_message_data():
    sql_command = "SELECT message.text, handle.id FROM message JOIN handle on message.handle_id=handle.ROWID"
    rval = common.fetch_db_data(DB_PATH, sql_command)

    data = []
    for row in rval:
        data.append(MessageData(row[1], row[0]))
    return data

def main():
    """
    The entry point of this program.
    """
    message_data = fetch_message_data()
    print(message_data)


if __name__ == '__main__':
    print('\n\n    ##### A Python script to read iMessage data #####')
    print('    #              Created by niftycode             #')
    print(f'    #                 Version {VERSION}                 #')
    print('    #################################################\n\n')
    print()
    main()
