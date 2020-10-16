#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch data, print data and export data to excel.
Python 3.8+
Author: niftycode
Date created: October 8th, 2020
Date modified: October 16th, 2020
"""


from os.path import expanduser
from imessage_reader import common
from imessage_reader import write_excel

# The path to the iMessage database
DB_PATH = expanduser("~") + '/Library/Messages/chat.db'


class MessageData:
    """
    This class is the store for the messages.
    """
    def __init__(self, user_id, text, service):
        """
        init function of this class
        :param user_id: The user id used in iMessage (mobile or email)
        :param text: The user's message
        :param service: SMS or iMessage
        """
        self.user_id = user_id
        self.text = text
        self.service = service

    def __str__(self):
        """
        :return: String representation of this object
        """
        return f"user id: {self.user_id}:\nmessage: {self.text}\nservice: {self.service}\n"


# noinspection PyMethodMayBeStatic
class FetchData:
    """
    This class contains the methods for fetch, print and export the messages.
    """
    def read_database(self) -> list:
        """
        Fetch data from the database and store the data in a list.
        :return: List containing the user id and the message
        """
        sql_command = "SELECT message.text, handle.id, handle.service" \
                      " FROM message JOIN handle on message.handle_id=handle.ROWID"
        rval = common.fetch_db_data(DB_PATH, sql_command)

        data = []
        for row in rval:
            data.append(MessageData(row[1], row[0], row[2]))
        return data

    def show_user_txt(self, export: bool):
        """
        Call fetch_message_data() method, print fetched data and export data.
        This method is for CLI usage.
        :param export: Determine whether to export data
        """

        fetched_data = self.read_database()

        # CLI output
        for data in fetched_data:
            print(data)

        # Excel export
        if export is True:
            self.export_data(fetched_data)

    def export_data(self, data: list):
        """
        Export data (write Excel file)
        This method is for CLI usage.
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
        service = []

        for data in fetched_data:
            users.append(data.user_id)
            messages.append(data.text)
            service.append(data.service)

        users_messages = list(zip(users, messages, service))

        return users_messages
