import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "column_text_format",
    version = "0.0.2",
    author = "Clark Fitzgerald, Julian Hernandez, Shawheen Naderi",
    author_email = "notsetupyet@gmail.com",
    description = ("Unfilled description"),
    license = "BSD",
    keywords = "Tabular data access",
    url = "http://packages.python.org/an_example_pypi_project",
    long_description_content_type='text/markdown',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Topic :: System :: Filesystems",
    ],
    # package_dir={"": "",
    # },
    packages=["column_text_format"],
)