#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch data, print data and export data to excel.
Python 3.8+
Author: niftycode
Date created: October 8th, 2020
Date modified: October 19th, 2020
"""


from dataclasses import dataclass
from os.path import expanduser
from imessage_reader import common
from imessage_reader import write_excel


@dataclass
class MessageData:
    """
    This dataclass is the store for the data
    (user id, message, imessage or sms service).
    """
    user_id: str
    text: str
    service: str

    def __str__(self):
        """
        :return: String representation of this object
        """
        return f"user id: {self.user_id}:\n" \
               f"message: {self.text}\n" \
               f"service: {self.service}\n"


# noinspection PyMethodMayBeStatic
class FetchData:
    """
    This class contains the methods for fetch, print and export the messages.
    """

    # The path to the iMessage database
    DB_PATH = expanduser("~") + '/Library/Messages/chat.db'

    # The SQL command
    SQL_CMD = "SELECT message.text, handle.id, handle.service " \
              "FROM message JOIN handle on message.handle_id=handle.ROWID"

    def read_database(self) -> list:
        """
        Fetch data from the database and store the data in a list.
        :return: List containing the user id, the message and the service
        """

        rval = common.fetch_db_data(self.DB_PATH, self.SQL_CMD)

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
        :param data: imessage objects containing user id, message and service
        """
        ew = write_excel.ExelWriter(data)
        ew.write_data()

    def get_messages(self) -> list:
        """
        Create a list with tuples (user id, message, service)
        :return: List with tuples (user id, message, service)
        """
        fetched_data = self.read_database()

        users = []
        messages = []
        service = []

        for data in fetched_data:
            users.append(data.user_id)
            messages.append(data.text)
            service.append(data.service)

        data = list(zip(users, messages, service))

        return data
