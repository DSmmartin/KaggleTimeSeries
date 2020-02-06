from setuptools import setup, find_packages
from os import path

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kaggle_web_traffic_forecasting",
    version="0.0.1",
    author="Manuel Martin",
    author_email="mmartin@plainconcepts.com",
    description="My ML package of Web traffic forecasting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ORG@dev.azure.com/ORG/kaggle_web_traffic_forecasting/_git/kaggle_web_traffic_forecasting_pkg",
    packages=find_packages(),
    install_requires=['Markdown'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)