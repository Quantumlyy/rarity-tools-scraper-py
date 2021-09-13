#!/bin/env python3
from setuptools import setup

setup(
    name="rarity-tools-scraper",
    version="0.0.3",
    url="https://github.com/quantumlyy/rarity-tools-scraper-py",
    author="Nejc Drobnič",
    author_email="yo@quantumly.dev",
    license="BSD-3-Clause",
    packages=["rarity_tools_scraper"],
    include_package_data=True,
    setup_requires="setuptools-pipfile",
    use_pipfile=True,
)
