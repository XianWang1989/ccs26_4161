
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Auto-detects all packages in your package directory
    py_modules=['plugin1', 'plugin2'],  # Include your plugin modules
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include the plugins in the package data
    },
    include_package_data=True,  # Make sure to include package data
    install_requires=[],  # Add any other dependencies your package needs
)
