"""
Testing python test-build-package-deploy.
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    # data_files=[('my_data', ['data/sample1.dat'])],
    # entry_points={
    #     'console_scripts': [
    #         'myapp=myapp.__main__:main',
    #     ],
    # },
    # test_suite="tests"
)