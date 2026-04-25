
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find packages in the 'mypackage' directory
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],  # Include the plugin files as top-level modules
    install_requires=[],  # Add your package dependencies here
)
