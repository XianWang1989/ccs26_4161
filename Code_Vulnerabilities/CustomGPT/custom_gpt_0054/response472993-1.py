
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'mypackage': ['*.py'],  # Include all Python files in the mypackage directory
    },
    include_package_data=True,  # This is required to include package_data files
    # Other parameters can be added (author, description, etc.)
)
