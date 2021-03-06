#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='ducktoolkit',
    version='0.9',
    author='Kevin Breen, James Hall',
    author_email='pip@ducktoolkit.com',
    description="USB Rubber Ducky Toolkit",
    url='https://ducktoolkit.com',
    license='GNU V3',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    scripts=['ducktools.py'],
    package_data={'': ['*.json', 'README.md, LICENSE']},
)
