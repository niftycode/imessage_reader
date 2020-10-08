from setuptools import setup, find_packages

setup(
    name='src',
    version='1.0.3',
    license='MIT',
    description='Fetch recipients and chat messages from the chat.db database.',

    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/imessage_reader',

    packages=find_packages(exclude=('tests', 'docs')),

    install_requires=['pytest'],
    tests_require=['pytest'],
)
