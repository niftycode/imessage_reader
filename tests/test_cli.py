#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from imessage_reader import cli


@pytest.fixture()
def create_parser():
    """
    Create a parser
    """
    parser = cli.get_parser()
    yield parser


def test_evaluate(create_parser):
    """
    Test if the given arguments will be parsed.
    :param create_parser: The created parser
    """
    args_version = create_parser.parse_args(["--version"])
    args_excel = create_parser.parse_args(["--excel"])
    args_sqlite = create_parser.parse_args(["--sqlite"])
    args_recipients = create_parser.parse_args(["--recipients"])

    assert args_version.version is True
    assert args_excel.excel is True
    assert args_sqlite.sqlite is True
    assert args_recipients.recipients is True
