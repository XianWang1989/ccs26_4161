
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    # Include your plugins in the package data
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include all plugins
    },
    include_package_data=True,
    install_requires=[],  # Add your dependencies here
)
