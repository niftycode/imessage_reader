import io

from setuptools import setup, find_packages

from imessage_reader import common

with io.open('README.md', 'rt', encoding='utf8') as f:
    LONG_DESC = f.read()


setup(
    name='imessage_reader',
    version=common.VERSION,
    license='MIT',
    description='Fetch recipients and chat messages from the chat.db database.',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/imessage_reader',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],

    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': ['imessage_reader=imessage_reader.cli:main'],
    },
    install_requires=['openpyxl'],
    tests_require=['pytest'],
)
