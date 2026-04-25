
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package that includes plugins',
    packages=find_packages(),  # Includes mypackage
    py_modules=['plugin1', 'plugin2'],  # Include your plugins as modules
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include the plugin files in the root package
    },
    include_package_data=True,  # Include package data files
    install_requires=[],  # List of dependencies
)
