#!/usr/bin/env python3

"""
App info, license, version
Python 3.9+
Date created: June 14th, 2020
Date modified: February 22nd, 2022
"""


from imessage_reader import common

VERSION = common.VERSION


def app_info():
    """Show app infos (Version & License)
    """
    print("\n\n    ##### A Python script to read iMessage data #####")
    print("    #              Created by niftycode             #")
    print(f"    #                 Version {VERSION}                 #")
    print("    #                  MIT License                  #")
    print("    #################################################\n\n")
    print()
