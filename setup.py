from setuptools import setup

setup(
    name="katas",
    version="0.1",
    description="A sample Python package",
    author="John Doe",
    author_email="jdoe@example.com",
    packages=["bowling_scoring", "fizzbuzz"],
    install_requires=[
        "black",
        "pytest",
    ],
)
