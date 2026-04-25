
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['*.py'],  # Include all .py files in the package
    },
    include_package_data=True,
    zip_safe=False,
)
