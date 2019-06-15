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

VERSION = '1.0.1'

# The path to the imessage database
# DB_PATH = '/Users/{0}/Library/Messages/chat.db'.format(os.getlogin())
DB_PATH = '/Users/{0}/Desktop/chat.db'.format(os.getlogin())  # for testing only


# TODO: Move class to separate file.
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


def fetch_recipients():
    sql_command = "SELECT ROWID, id from handle"
    rval = common.fetch_db_data(DB_PATH, sql_command)

    recipients = []
    for row in rval:
        recipients.append(Recipient(row[0], row[1]))

    return recipients


def fetch_messages():
    sql_command = "SELECT text, handle_id from message"
    rval = common.fetch_db_data(DB_PATH, sql_command)

    messages = []
    for row in rval:
        messages.append(Messages(row[0], row[1]))

    return messages


def main():
    """
    The entry point of this program.
    """
    # recipients = fetch_recipients()
    #
    # first_recipient = recipients[0]
    # print(first_recipient.rowid)
    # print(first_recipient.phone_id)

    messages = fetch_messages()
    for i in messages:
        print(i)


if __name__ == '__main__':
    print('\n\n    ##### A Python script to read iMessage data #####')
    print('    #              Created by niftycode             #')
    print(f'    #                 Version {VERSION}                 #')
    print('    #################################################\n\n')
    print()
    main()
