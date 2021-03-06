#!/usr/bin/env python3

from setuptools import setup, find_packages

f = open('README.rst', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='lumache',
    version='1.0',
    description='rtd-test',
    long_description=LONG_DESCRIPTION,
    keywords=['Documentation', ],
    author='glozanoa',
    author_email='glozanoa@uni.pe',
    url='https://github.com/glozanoa/test-rtd',
    license='GPL-3',
    classifiers = [
        "Programming Language :: Python :: 3.9",
    ],
    py_modules=['lumache'],
    include_package_data=True,
)
