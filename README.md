# imessage_reader

![](img/license-MIT-green.svg) ![](img/python-3.8-blue.svg) ![](https://img.shields.io/github/last-commit/niftycode/imessage_reader.svg?style=flat) ![](https://img.shields.io/github/issues/niftycode/imessage_reader.svg?style=flat)

This is a forensic tool written in Python 3. Use this tool to fetch the content (phone numbers, email addresses and messages) from the *chat.db* database file on **macOS** (version 10.14 or above).

## Background

Received messages (iMessage or SMS) and attachments will be saved in "~/Library/Messages". This directory contains a "chat.db" file (SQLite3) with two tables of interest: *handle* and *message*. The *handle* table contains the recipients (email address or phone number). The received messages are in the *message* table.

## Requirements

* **Python 3.8+**
* pytest
* openpyxl
* setuptools

## Install

    pip3 install imessage_reader

## Usage

Start the program with:

    imessage_reader

This will show you all users and messages.

Use

    imessage_reader.py -e

to create an Excel file containing users and messages.

**Note**: You need access to the *Library* folder in order to read the iMessage database file ("chat.db"). You can add access (for *Terminal* or *iTerm*) in

    > System Preferences > Security & Privacy > Privacy > Full Disk Access

## ToDo

* Fetch the date of received messages.
* Show a list of all known recipients.
* Did the user receive the message via SMS or via iMessage?
* Show attachments.
* Add more tests.

## Changelog

see [CHANGELOG.rst](CHANGELOG.rst)
