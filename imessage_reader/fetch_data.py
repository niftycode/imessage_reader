#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch data, print data and export data to excel.
Python 3.8+
Author: niftycode
Date created: October 8th, 2020
Date modified: October 27th, 2020
"""


import sys
from dataclasses import dataclass
from os.path import expanduser
from imessage_reader import common
from imessage_reader import write_excel
from imessage_reader import create_sqlite


@dataclass
class MessageData:
    """
    This dataclass is the store for the data
    (user id, message, imessage or sms service).
    """
    user_id: str
    text: str
    date: str
    service: str

    def __str__(self):
        """
        :return: String representation of this object
        """
        return f"user id: {self.user_id}:\n" \
               f"message: {self.text}\n" \
               f"date: {self.date}\n" \
               f"service: {self.service}\n"


# noinspection PyMethodMayBeStatic
class FetchData:
    """
    This class contains the methods for fetch, print and export the messages.
    """

    # The path to the iMessage database
    DB_PATH = expanduser("~") + '/Library/Messages/chat.db'

    # The SQL command
    SQL_CMD = "SELECT " \
              "text, " \
              "datetime((date / 1000000000) + 978307200, 'unixepoch', 'localtime')," \
              "handle.id, " \
              "handle.service " \
              "FROM message " \
              "JOIN handle on message.handle_id=handle.ROWID"

    def __init__(self, system=None):
        if system is None:
            self.operating_system = common.get_platform()

    def _check_system(self):
        if self.operating_system != 'MAC':
            sys.exit("Your operating system is not supported yet!")

    def _read_database(self) -> list:
        """
        Fetch data from the database and store the data in a list.
        :return: List containing the user id, the message and the service
        """

        rval = common.fetch_db_data(self.DB_PATH, self.SQL_CMD)

        data = []
        for row in rval:
            data.append(MessageData(row[2], row[0], row[1], row[3]))
        return data

    def show_user_txt(self, export: str):
        """
        Call fetch_message_data() method, print fetched data and export data.
        This method is for CLI usage.
        :param export: Determine whether to export data
        """

        # Check the running operating system
        self._check_system()

        # Read chat.db
        fetched_data = self._read_database()

        # CLI output
        for data in fetched_data:
            print(data)

        # Excel export
        if export == 'excel':
            self._export_excel(fetched_data)

        # SQLite3 export
        if export == 'sqlite':
            self._export_sqlite(fetched_data)

    def _export_excel(self, data: list):
        """
        Export data (write Excel file)
        :param data: imessage objects containing user id, message and service
        """
        file_path = expanduser("~") + '/Desktop/'
        ew = write_excel.ExelWriter(data, file_path)
        ew.write_data()

    def _export_sqlite(self, data: list):
        """
        Export data (create SQLite3 database)
        :param data: imessage objects containig user id, message and service
        """
        file_path = expanduser("~") + '/Desktop/'
        cd = create_sqlite.CreateDatabase(data, file_path)
        cd.create_sqlite_db()

    def get_messages(self) -> list:
        """
        Create a list with tuples (user id, message, date, service)
        This method is for CLI usage.
        :return: List with tuples (user id, message, date, service)
        """
        fetched_data = self._read_database()

        users = []
        messages = []
        dates = []
        service = []

        for data in fetched_data:
            users.append(data.user_id)
            messages.append(data.text)
            dates.append(data.date)
            service.append(data.service)

        data = list(zip(users, messages, dates, service))

        return data
