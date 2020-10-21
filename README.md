# imessage_reader

![](img/license-MIT-green.svg) ![](img/python-3.8-blue.svg) ![](https://img.shields.io/github/last-commit/niftycode/imessage_reader.svg?style=flat) ![](https://img.shields.io/github/issues/niftycode/imessage_reader.svg?style=flat)

This is a forensic tool written in Python 3. Use this tool to fetch the content (phone numbers, email addresses and messages) from the *chat.db* database file on **macOS** (version 10.14 or above).

## Background

Received messages (iMessage or SMS) and attachments will be saved in "~/Library/Messages". This directory contains a "chat.db" file (SQLite3) with two tables of interest: *handle* and *message*. The *handle* table contains the recipients (email address or phone number). The received messages are in the *message* table.

## Note

Since the iMessage database is only available under macOS, it makes no sense to use this tool under Windows or Linux.

## Requirements

* **Python 3.8+**
* openpyxl

## Install

    pip3 install imessage_reader

## Usage (CLI)

Start the program with:

    imessage_reader

This will show you all users and messages.

Use

    imessage_reader.py -e

to create an Excel file containing users and messages. The file will be stored in the Desktop folder.

**Note**: You need access to the *Library* folder in order to read the iMessage database file ("chat.db"). You can add access (for *Terminal* or *iTerm*) in

    > System Preferences > Security & Privacy > Privacy > Full Disk Access

## Usage (import module)

To get the messages use following code:

    from imessage_reader import fetch_data

    # Create a FetchData instance
    fd = fetch_data.FetchData()

    # Store messages in my_data
    # This is a list of tuples containing user id, message and service.
    # service -> iMessage or SMS
    my_data = fd.get_messages()
    print(my_data)

## ToDo

* Get the date of messages
* Fetch the date of received messages.
* Show a list of all known recipients.
* ~~Did the user receive the message via SMS or via iMessage?~~
* Show attachments.
* Add more tests.

## Changelog

see [CHANGELOG.rst](https://github.com/niftycode/imessage_reader/blob/master/CHANGELOG.rst)
