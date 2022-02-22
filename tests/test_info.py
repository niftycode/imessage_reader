#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from imessage_reader import common
from imessage_reader import info


@pytest.fixture()
def app_version():
    return common.VERSION


def test_app_info(app_version):
    assert info.VERSION == app_version
