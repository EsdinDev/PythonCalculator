#### setup.py
from setuptools import setup, find_packages

setup(
    name=repr('my_project'),
    version=repr('0.1'),
    packages=find_packages(where=repr('src')),
    package_dir={repr(''): repr('src')},
)