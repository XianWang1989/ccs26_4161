
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include plugin files as modules
    install_requires=[],  # Add any dependencies if needed
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include the plugins
    },
    include_package_data=True,  # Make sure to include package data
    description='My Awesome Package with Plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://example.com/mypackage',
)
