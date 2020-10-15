.. gtrending documentation master file, created by
   sphinx-quickstart on Tue Aug 11 09:36:45 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to gtrending's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Lightweight and easy-to-use python library for fetching
trending repositories and developers. Relies on
`github-trending-api
<https://github.com/huchenme/github-trending-api>`_
which is in JavaScript, so gtrending aims to fill the gap
for python.

Simple example, fetching the trending python projects and
display their full names::

    from gtrending import fetch_repos

    repos = fetch_repos(language="python")  # get the result as a dict

    for repo in repos:
        print(repo["fullname"])  # full name (user/repo) of each repo


Features
--------

- Fetching repos/developers by language, and time range
- Fast and efficient
- returns complete data
- pytest-ed


Installation
------------

Install gtrending by running::

    pip install gtrending

Contribute
----------

- Issue Tracker: https://github.com/hedythedev/gtrending/issues
- Source Code: https://github.com/hedythedev/gtrending

Support
-------

If you are having issues, please raise an issue on github.


License
-------

The project is licensed under the MIT license.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
