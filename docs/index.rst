.. gtrending documentation master file, created by
   sphinx-quickstart on Tue Aug 11 09:36:45 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to imessage_reader's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


A python library for fetching data from the chat.db database on macOS.

To fetch users and messages use the following code::

    from imessage_reader import fetch_data

    data = fetch_data.FetchData()  # create an instance
    fetched_messages = data.get_messages()  # get the result as a list

You will retrieve a list with tuples containing a user id with the message.

Use imessage_reader on the command line with following command::

   imessage_reader  # show users and messages on the command line
   imessage_reader -e  # additionally, export data to Excel
   imessage_reader -v  # show version and license

Features
--------

- Fetching users and imessages
- Can also be used on the command line


Installation
------------

Install imessage_reader by running::

    pip install imessage_reader

Contribute
----------

- Issue Tracker: https://github.com/niftycode/imessage_reader/issues
- Source Code: https://github.com/niftycode/imessage_reader

Support
-------

If you have a comment or find a bug, please leave an issue on Github.


License
-------

The project is licensed under the MIT license.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
