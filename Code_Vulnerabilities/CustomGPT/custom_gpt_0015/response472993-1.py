
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'mypackage': ['*'],  # Include all files in mypackage directory
        '': ['*.py'],  # Include all Python files in the root directory
    },
    include_package_data=True,
    install_requires=[],  # Add any dependencies here
)
