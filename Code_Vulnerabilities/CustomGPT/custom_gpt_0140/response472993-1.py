
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include the plugin files as modules
    install_requires=[],  # Add any dependencies here
    include_package_data=True,
)
