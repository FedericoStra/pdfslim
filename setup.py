#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="pdfslim",
    version="1.1.0",
    description="`pdfslim` takes a number of PDF files and tries to optimize them through a suitable call to `ghostscript`.",
    license="GPLv3",
    author="Federico Stra",
    author_email="stra.federico@gmail.com",
    url="https://github.com/FedericoStra/pdfslim",
    project_urls={
        "Code": "https://github.com/FedericoStra/pdfslim",
        "Issue tracker": "https://github.com/FedericoStra/pdfslim/issues",
    },
    # packages=find_packages(),
    py_modules=["pdfslim"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pdfslim=pdfslim:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = 'PDF, GhostScript',
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Office/Business",
        "Topic :: System :: Archiving :: Compression",
        "Topic :: Utilities",
    ],
)
