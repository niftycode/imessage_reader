#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from imessage_reader import common

VERSION = '1.0.0'

# The path to the imessage database
DB_PATH = '/Users/{0}/Library/Messages/chat.db'.format(os.getlogin())


# TODO - 14.06.2019: Move this class to a separate file.
class Recipient:
    def __init__(self, id, identifier):
        self.id = id
        self.identifier = identifier

    def __repr__(self):
        return f"id: {self.id}"


def fetch_recipients():
    


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


if __name__ == '__main__':
    print('\n\n    #### A Python script to analyze browser data ####')
    print('    #               Created by niftycode            #')
    print(f'    #                  Version {VERSION}                #')
    print('    #################################################\n\n')
    print()
    main()
