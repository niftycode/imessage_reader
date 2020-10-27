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
    args_version = create_parser.parse_args(['--version'])
    args_excel = create_parser.parse_args(['--excel'])
    assert args_version.version is True
    assert args_excel.excel is True
