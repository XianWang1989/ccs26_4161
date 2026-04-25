
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # To include non-Python files
    py_modules=['plugin1', 'plugin2'],  # Declare your plugins
    install_requires=[],  # List any dependencies your package requires
)
