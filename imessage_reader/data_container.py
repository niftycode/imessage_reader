#!/usr/bin/env python3

"""
Data Container
Python 3.9+
Author: niftycode
Modified by: -
Date created: February 19th, 2022
Date modified: -
"""

from dataclasses import dataclass


@dataclass
class MessageData:
    """This dataclass is the store for the data:
    user id, text, date, service and account (caller id).
    """

    user_id: str
    text: str
    date: str
    service: str
    account: str
    is_from_me: int

    def __str__(self):
        """String representation

        :return: the representation of this object
        """
        return (
            f"user id:\t\t{self.user_id}\n"
            f"date and time:\t\t{self.date}\n"
            f"service:\t\t{self.service}\n"
            f"caller id:\t\t{self.account}\n"
            f"is_from_me:\t\t{self.is_from_me}\n"
            f"\n"
            f"text:\n"
            f"=====\n"
            f"{self.text}\n"
            f"\n"
            f"----------------------------------------------------------------\n"
        )
