#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import sqlite3
import os
from imessage_reader import common


@pytest.fixture(scope="function")
def initialize_db(tmpdir):
    file = os.path.join(tmpdir.strpath, "test.db")
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    cur.executescript(
        """
    DROP TABLE IF EXISTS handle;

    CREATE TABLE handle (
    ROWID   INTEGER UNIQUE,
    id      TEXT UNIQUE
    );
    """
    )

    cur.execute(
        """INSERT OR IGNORE INTO handle(ROWID, id)
        VALUES ( ?, ?)""",
        (8, "max@mustermann.de"),
    )

    conn.commit()

    yield file
    conn.close()


def test_fetch_db_data(initialize_db):
    sql_command = "SELECT ROWID, id from handle"
    rval = common.fetch_db_data(initialize_db, sql_command)
    assert isinstance(rval, object)
    assert rval == [(8, "max@mustermann.de")]
