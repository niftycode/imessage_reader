# Contributing

**Working on your first Pull Request?** You can learn how from this *free*
series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

## Reporting issues and providing feedback

If you find any bugs, be sure to open up an issue. Or you email me: [py@bodo-schoenfeld.de](mailto:py@bodo-schoenfeld.de).

## Development Dependencies

- Python 3 (versions 3.8+ are currently supported)
- `pip3 install flake8 pytest`
    - `flake8` to check for errors and to enforce code style.
    - `pytest` to run the tests (optional, you can contribute without writing tests).
- Install all requirements with the following command:

        pip3 install -r requirements_dev.txt

- If you're making changes to the documentation, install the documentation
  dependencies: `pip3 install -r docs/requirements.txt`.
- You can find
  a [brief introduction to reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) in the Sphinx documentation.

**Note**: This project uses **absolute imports** ([recommended by PEP8](https://www.python.org/dev/peps/pep-0008/#imports)). So, you'd be better off using a **virtual environment** and run

    python3 setup.py install --user

## Development Process

- Select an issue to work on.
- Fork and clone the repository, create a **virtual environment** and install all the dependencies:

        $ pip3 install -r requirements_dev.txt

- Work on the master branch for smaller patches or create a **separate branch for new features**.
- Make changes, `git add` and then commit. You can link to the issue number in the commit message (optional).
- (Optional) Run `flake8` and `pytest`.
- (Optional) If you're updating the documentation, make sure you update `docs/index.rst` and `README.md` simultaneously.
- Use the GitHub website to create a Pull Request (PR) and wait for the maintainers to review it.
