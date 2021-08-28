#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import os
import sqlite3
from imessage_reader import common
from imessage_reader.fetch_data import MessageData


@pytest.fixture()
def message_data_one_row():
    return MessageData('max.mustermann@icloud.com',
                       'Hello!',
                       '2020-10-27 17:19:20',
                       'SMS',
                       '+01 555 17172',
                       1)


@pytest.fixture(scope='function')
def initialize_db(tmpdir):
    file = os.path.join(tmpdir.strpath, 'chat.db')
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS message;

    CREATE TABLE message (
    user_id     TEXT UNIQUE,
    text        TEXT UNIQUE,
    date        TEXT UNIQUE,
    service     TEXT UNIQUE,
    account     TEXT UNIQUE,
    is_from_me  INTEGER
    );
    ''')

    cur.execute('''INSERT OR IGNORE INTO message(user_id, text, date, service, account, is_from_me)
        VALUES ( ?, ?, ?, ?, ?, ?)''',
                ('max@mustermann.de',
                 'Hello Kendra!',
                 '2020-10-27 17:19:20',
                 'iMessage',
                 '+01 555 17172',
                 1))

    conn.commit()

    yield file
    conn.close()


def test_message_data(message_data_one_row):
    assert(isinstance(message_data_one_row, object))


def test_db_data(initialize_db):
    sql_command = 'SELECT user_id, text, date, service, account, is_from_me from message'
    rval = common.fetch_db_data(initialize_db, sql_command)
    assert(isinstance(rval, list))
    assert(isinstance(rval[0][0], str))
    assert (isinstance(rval[0][1], str))
    assert (isinstance(rval[0][2], str))
    assert (isinstance(rval[0][3], str))
    assert (isinstance(rval[0][4], str))
    assert (isinstance(rval[0][5], int))
