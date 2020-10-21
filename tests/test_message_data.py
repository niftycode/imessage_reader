#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import os
import sqlite3
from imessage_reader import common
from imessage_reader import fetch_data
from imessage_reader.fetch_data import MessageData


@pytest.fixture()
def message_data_one_row():
    return MessageData('max.mustermann@icloud.com', 'Hello!', 'SMS')


@pytest.fixture(scope='function')
def initialize_db(tmpdir):
    file = os.path.join(tmpdir.strpath, "chat.db")
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS message;

    CREATE TABLE message (
    user_id     TEXT UNIQUE,
    text        TEXT UNIQUE,
    service     TEXT UNIQE
    );
    ''')

    cur.execute('''INSERT OR IGNORE INTO message(user_id, text, service)
        VALUES ( ?, ?, ?)''', ('max@mustermann.de', 'Hello Kendra!', 'iMessage'))

    conn.commit()

    yield file
    conn.close()


def test_message_data(message_data_one_row):
    assert(isinstance(message_data_one_row, object))


def test_db_data(initialize_db):
    sql_command = "SELECT user_id, text, service from message"
    rval = common.fetch_db_data(initialize_db, sql_command)
    assert(isinstance(rval, list))
    assert(isinstance(rval[0][0], str))
    assert (isinstance(rval[0][1], str))
    assert (isinstance(rval[0][2], str))


def test_read_database():
    fd = fetch_data.FetchData()
    rval = fd.read_database()
    assert isinstance(rval, list)
