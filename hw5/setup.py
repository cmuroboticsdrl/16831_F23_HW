# setup.py
from setuptools import setup, find_packages

setup(
    name='rob831',
    version='0.1.0',
    packages=find_packages(),
    package_data={'':['*.xml']},
    include_package_data=True
)
