#!/usr/bin/env python3

from setuptools import setup, find_packages

readme = open('README.rst').read()
version = exec(open('mris/version.py').read())

setup(
    name='mris',
    version=__version__,
    description='Python wrapper for mris.',
    long_description=readme,
    author='Al Johri',
    author_email='al.johri@gmail.com',
    url='https://github.com/AlJohri/mris',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests', 'cssselect', 'lxml', 'blessings', 'arrow'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mris=mris.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ]
)
