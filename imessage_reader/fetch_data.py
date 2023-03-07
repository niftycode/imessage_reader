#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch data, print data and export data to excel.
Python 3.8+
Author: niftycode
Modified by: thecircleisround
Date created: October 8th, 2020
Date modified: February 19th, 2022
"""

import sys

from os.path import expanduser

from imessage_reader import common, create_sqlite, write_excel, data_container


# noinspection PyMethodMayBeStatic
class FetchData:
    """
    This class contains the methods to fetch, print and export the messages.
    """

    # The path to the iMessage database
    DB_PATH = expanduser("~") + "/Library/Messages/chat.db"

    # The SQL command
    SQL_CMD = (
        "SELECT "
        "text, "
        "datetime((date / 1000000000) + 978307200, 'unixepoch', 'localtime'),"
        "handle.id, "
        "handle.service, "
        "message.destination_caller_id, "
        "message.is_from_me, "
        "message.attributedBody, "
        "message.cache_has_attachments "
        "FROM message "
        "JOIN handle on message.handle_id=handle.ROWID"
    )

    def __init__(self, system=None):
        if system is None:
            self.operating_system = common.get_platform()

    def _check_system(self):
        if self.operating_system != "MAC":
            sys.exit("Your operating system is not supported yet!")

    def _read_database(self) -> list:
        """
        Fetch data from the database and store the data in a list.
        :return: List containing the user id, messages, the service and the account
        """

        rval = common.fetch_db_data(self.DB_PATH, self.SQL_CMD)

        data = []
        for row in rval:
            text = row[0]
            if row[7] == 1:
                text = "<Message with no text, but an attachment.>"
            # the chatdb has some weird behavior where sometimes the text value is None
            # and the text string is buried in an binary blob under the attributedBody field.
            if text is None and row[6] is not None:
                try:
                    text = row[6].split(b'NSString')[1]
                    text = text[5:]  # stripping some preamble which generally looks like this: b'\x01\x94\x84\x01+'

                    if text[0] == 129:  # this 129 is b'\x81, python indexes byte strings as ints, this is equivalent to text[0:1] == b'\x81'
                        length = int.from_bytes(text[1:3], 'little')
                        text = text[3:length + 3]
                    else:
                        length = text[0]
                        text = text[1:length + 1]
                    text = text.decode()
                except Exception as e:
                    print("ERROR: Can't read a message.")
                    print(e)

            data.append(
                data_container.MessageData(
                    row[2], text, row[1], row[3], row[4], row[5]
                )
            )

        return data

    def show_user_txt(self, export: str):
        """
        Invoke _read_database(), print fetched data and export data.
        This method is for CLI usage.
        :param export: Determine whether to export data
        """

        # Check the running operating system
        self._check_system()

        # Read chat.db
        fetched_data = self._read_database()

        # CLI output
        if export == "nothing":
            for data in fetched_data:
                print(data)

        # Excel export
        if export == "excel":
            self._export_excel(fetched_data)

        # SQLite3 export
        if export == "sqlite":
            self._export_sqlite(fetched_data)

        if export == "recipients":
            self._get_recipients()

    def _export_excel(self, data: list):
        """
        Export data (write Excel file)
        :param data: message objects containing user id, message, date, service, account
        """
        file_path = expanduser("~") + "/Desktop/"
        ew = write_excel.ExelWriter(data, file_path)
        ew.write_data()

    def _export_sqlite(self, data: list):
        """
        Export data (create SQLite3 database)
        :param data: message objects containig user id, message, date, service, account
        """
        file_path = expanduser("~") + "/Desktop/"
        cd = create_sqlite.CreateDatabase(data, file_path)
        cd.create_sqlite_db()

    def _get_recipients(self):
        """
        Create a list containing all recipients and
        show the recipients in the command line.
        """
        fetched_data = self._read_database()

        # Create a list with recipients
        recipients = [i.user_id for i in fetched_data if i.is_from_me == 0]

        print()
        print("List of Recipients")
        print("------------------------")
        print()

        for recipient in recipients:
            print(recipient)

    def get_messages(self) -> list:
        """
        Create a list with tuples (user id, message, date, service, account, is_from_me)
        This method is for module usage.
        :return: List with tuples (user id, message, date, service, account, is_from_me)
        """
        fetched_data = self._read_database()

        users = []
        messages = []
        dates = []
        service = []
        account = []
        is_from_me = []

        for data in fetched_data:
            users.append(data.user_id)
            messages.append(data.text)
            dates.append(data.date)
            service.append(data.service)
            account.append(data.account)
            is_from_me.append(data.is_from_me)

        data = list(zip(users, messages, dates, service, account, is_from_me))

        return data
