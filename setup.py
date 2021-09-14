#!/bin/env python3
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="rarity-tools-scraper",
    version="0.0.9",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quantumlyy/rarity-tools-scraper-py",
    author="Nejc Drobnič",
    author_email="yo@quantumly.dev",
    license="BSD-3-Clause",
    packages=["rarity_tools_scraper"],
    include_package_data=True,
    setup_requires="setuptools-pipfile",
    use_pipfile=True,
)
