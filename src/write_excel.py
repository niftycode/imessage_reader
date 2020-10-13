#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Write Excel file containing iMessage data (user id, text)
Python 3.8+
Date created: October 1st, 2020
Date modified: October 8th, 2020
"""

import openpyxl
from openpyxl.styles import Font
from os.path import expanduser


EXCEL_FILE_PATH = expanduser("~") + '/Desktop/'


class ExelWriter:

    def __init__(self, imessage_data: list):
        """
        init function of this class
        :param imessage_data: List with iMessage data objects containing user id and text
        """
        self.imessage_data = imessage_data

    def write_data(self):
        """
        Write data (user id, text) to Excel
        """

        users = []
        messages = []

        for data in self.imessage_data:
            users.append(data.user_id)
            messages.append(data.text)

        # TODO: Add exception handling
        # Call openpyxl.Workbook() to create a new blank Excel workbook
        workbook = openpyxl.Workbook()

        # Activate a sheet
        sheet = workbook.active

        # Set a title
        sheet.title = 'iMessages'

        # Set headline style
        bold16font = Font(size=16, bold=True)

        sheet['A1'] = 'User'
        sheet['A1'].font = bold16font

        sheet['B1'] = 'Message'
        sheet['B1'].font = bold16font

        users_row = 2

        # Write users to 1st column
        for user in users:
            sheet.cell(row=users_row, column=1).value = user
            users_row += 1

        messages_row = 2

        # Write messages to 2nd column
        for message in messages:
            sheet.cell(row=messages_row, column=2).value = message
            messages_row += 1

        # Save the workbook (excel file)
        # TODO: Create file name with date
        workbook.save(EXCEL_FILE_PATH + 'iMessage-Data.xlsx')

        print("Excel file successfully created!")
