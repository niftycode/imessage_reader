#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Create a SQLite3 database containing iMessage data (user id, text, date, service)
Python 3.9+
Date created: April 30th, 2021
Date modified: August 28th, 2021
"""

import sqlite3


class CreateDatabase:
    """This class manages the export to SQLite.
    """

    def __init__(self, imessage_data: list, file_path: str):
        """Constructor method

        :param imessage_data: list with MessageData objects
                containing user id, text, date, service and account
        :param file_path: the path to the location of the Excel file
        """
        self.imessage_data = imessage_data
        self.file_path = file_path

    def create_sqlite_db(self):
        """Create a SQLite3 database in the Desktop folder.
        Add user, text, date and service to the database.
        """
        database = self.file_path + "iMessage-Data.sqlite"

        conn = sqlite3.connect(database)
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS Messages")

        cur.execute(
            """
        CREATE TABLE IF NOT EXISTS Messages (user_id TEXT,
        message TEXT,
        date TEXT,
        service TEXT,
        destination_caller_id TEXT, 
        is_from_me TEXT)"""
        )

        for data in self.imessage_data:
            cur.execute(
                """INSERT INTO Messages (user_id, message, date, service, destination_caller_id, is_from_me)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (
                    data.user_id,
                    data.text,
                    data.date,
                    data.service,
                    data.account,
                    data.is_from_me,
                ),
            )

        conn.commit()
        cur.close()

        print()
        print(">>> SQLite database successfully created! <<<")
        print("You find the Database in your Documents folder.")
        print()
