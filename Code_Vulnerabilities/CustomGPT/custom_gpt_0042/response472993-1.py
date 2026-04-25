
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find packages in the mypackage directory
    package_data={
        'mypackage': ['*.py'],   # Include all .py files in mypackage directory
    },
    include_package_data=True,   # Include package data as defined in package_data
    scripts=['plugin1.py', 'plugin2.py'],  # Install plugins as scripts
    zip_safe=False,  # Keeps plugins easily accessible for use
)
