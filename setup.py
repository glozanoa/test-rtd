#!/usr/bin/env python3

from setuptools import setup, find_packages

f = open('README.rst', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='lumache',
    version=VERSION,
    description='rtd-test',
    long_description=LONG_DESCRIPTION,
    keywords=['Documentation', ],
    author='glozanoa',
    author_email='glozanoa@uni.pe',
    url='https://github.com/glozanoa/test-rtd',
    license=LICENSE,
    classifiers = [
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
)
