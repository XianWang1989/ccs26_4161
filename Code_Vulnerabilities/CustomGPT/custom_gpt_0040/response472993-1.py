
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'mypackage': ['*.py'],
    },
    include_package_data=True,
    install_requires=[],
)
