#####################################################
# Copyright (c) Xuanyi Dong [GitHub D-X-Y], 2021.09 #
#####################################################
"""The setup function for pypi."""
# The following is to make nats_bench avaliable on Python Package Index (PyPI)
#
# conda install -c conda-forge twine  # Use twine to upload nats_bench to pypi
#
# python setup.py sdist bdist_wheel
# python setup.py --help-commands
# twine check dist/*
#
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*
# https://pypi.org/project/awesome_autodl
#
# TODO(xuanyidong): upload it to conda
#
import os
import glob
from pathlib import Path
from setuptools import setup, find_packages
from awesome_autodl import version

NAME = "awesome_autodl"
REQUIRES_PYTHON = ">=3.6"
DESCRIPTION = "Package for Automated Deep Learning Paper Analysis"

VERSION = version()


def read(fname="README.md"):
    with open(
        os.path.join(os.path.dirname(__file__), fname), encoding="utf-8"
    ) as cfile:
        return cfile.read()


# What packages are required for this module to be executed?
REQUIRED = ["pyyaml>=5.0.0"]

packages = find_packages(exclude=("tests", "checklist", "docs"))
print(f"packages: {packages}")


def find_yaml(xdir, cur_depth=1, max_depth=1):
    xdirs = []
    for xfile in Path(xdir).glob("*"):
        if xfile.is_dir() and cur_depth < max_depth:
            xdirs += find_yaml(xfile, cur_depth + 1, max_depth)
        elif xfile.name.endswith(".yaml"):
            xdirs.append(str(xfile))
    return xdirs


setup(
    name=NAME,
    version=VERSION,
    author="Xuanyi Dong",
    author_email="dongxuanyi888@gmail.com",
    description=DESCRIPTION,
    license="MIT Licence",
    keywords="NAS Dataset API DeepLearning",
    url="https://github.com/D-X-Y/Awesome-AutoDL",
    packages=packages,
    data_files=[
        (f"{NAME}/raw_data", find_yaml(f"{NAME}/raw_data")),
        (f"{NAME}/raw_data/papers", find_yaml(f"{NAME}/raw_data/papers")),
    ],
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
    ],
)
