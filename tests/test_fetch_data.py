#!/usr/bin/env python3

from imessage_reader import fetch_data


data = fetch_data.FetchData("/Users/bodo/Documents")


def test_fetch_data(mocker):
    mocker.patch("imessage_reader.fetch_data.FetchData.__init__",
                 db_path="/Users/bodo/Documents",
                 system=None)
    input_path = data.db_path
    input_system = data.operating_system
    assert input_path == "/Users/bodo/Documents"
    assert not None
