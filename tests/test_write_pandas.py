#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from imessage_reader.data_container import MessageData
from imessage_reader.write_pandas import DataFrameWriter

@pytest.fixture
def message_data_one_row():
    message_data_list = [
        MessageData(
            user_id="max.mustermann@icloud.com",
            text="Hello!",
            date="2020-10-27 17:19:20",
            service="SMS",
            account="+01 555 17172",
            is_from_me=1,
        )
    ]
    return message_data_list

def test_dataframe_output(message_data_one_row):
    # Initialize DataFrameWriter with test data
    writer = DataFrameWriter(message_data_one_row)
    df = writer.to_dataframe()
    
    # Expected DataFrame content
    expected_data = {
        'User ID': ["max.mustermann@icloud.com"],
        'Message': ["Hello!"],
        'Date': ["2020-10-27 17:19:20"],
        'Service': ["SMS"],
        'Account': ["+01 555 17172"],
        'Is From Me': [1],
    }
    expected_df = pd.DataFrame(expected_data)
    
    # Check if the DataFrame has the expected content
    pd.testing.assert_frame_equal(df, expected_df)
