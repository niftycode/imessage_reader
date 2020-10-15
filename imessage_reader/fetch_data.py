#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch data, print data and export data to excel.
Python 3.8+
Author: niftycode
Date created: October 8th, 2020
Date modified: October 13th, 2020
"""


from os.path import expanduser
from imessage_reader import common
from imessage_reader import write_excel

# The path to the iMessage database
DB_PATH = expanduser("~") + '/Library/Messages/chat.db'


def iterable(cls):
    def iterfn(self):
        iters = dict((x, y) for x, y in cls.__dict__.items() if x[:2] != '__')
        iters.update(self.__dict__)

        for x, y in iters.items():
            yield x, y

    cls.__iter__ = iterfn
    return cls


class Recipient:
    """
    This class is currently not used!
    """
    # TODO: Fetch row id and phone id

    def __init__(self, rowid, phone_id):
        """
        init function of this class
        :param rowid: The unique row id of the database
        :param phone_id: The phone id
        """
        self.rowid = rowid
        self.phone_id = phone_id

    def __repr__(self):
        """
        :return: String representation of this object
        """
        return f"{self.rowid}: {self.phone_id}"


class MessageData:
    def __init__(self, user_id, text):
        """
        init function of this class
        :param user_id: The user id used in iMessage (mobile or email)
        :param text: The user's message
        """
        self.user_id = user_id
        self.text = text

    def __repr__(self):
        """
        :return: String representation of this object
        """
        return f"{self.user_id}: {self.text}\n\n"


# noinspection PyMethodMayBeStatic
class FetchData:

    def read_database(self) -> list:
        """
        Fetch data from the database and store the data in a list.
        :return: List containing the user id and the message
        """
        sql_command = "SELECT message.text, handle.id FROM message JOIN handle on message.handle_id=handle.ROWID"
        rval = common.fetch_db_data(DB_PATH, sql_command)

        data = []
        for row in rval:
            data.append(MessageData(row[1], row[0]))
        return data

    def show_user_txt(self, export: bool):
        """
        Call fetch_message_data() method, print fetched data and export data.
        :param export: Determine whether to export data
        """

        fetched_data = self.read_database()

        for data in fetched_data:
            print(data)

        if export is True:
            self.export_data(fetched_data)

    def export_data(self, data: list):
        """
        Export data (Write excel file)
        :param data: imessage objects containing user id and text
        """
        ew = write_excel.ExelWriter(data)
        ew.write_data()

    def get_messages(self) -> list:
        """
        Create a list with tuples (user id, message)
        :return: List with tuples (user id, message)
        """
        fetched_data = self.read_database()

        users = []
        messages = []

        for data in fetched_data:
            users.append(data.user_id)
            messages.append(data.text)

        users_messages = list(zip(users, messages))

        return users_messages
