#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import platform
from imessage_reader import common


@pytest.fixture(scope="function")
def get_os():
    operating_system = platform.system()
    if operating_system == "Darwin":
        yield "MAC"
    if operating_system == "Windows":
        yield "WINDOWS"
    if operating_system == "Linux":
        yield "LINUX"


def test_get_platform(get_os):
    current_os = common.get_platform()
    expected_os = get_os
    assert current_os == expected_os
