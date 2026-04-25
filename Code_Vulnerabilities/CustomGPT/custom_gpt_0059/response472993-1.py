
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find packages
    py_modules=['plugin1', 'plugin2'],  # Include the plugins as standalone modules
    include_package_data=True,  # Include all files in the distribution
    zip_safe=False,
)
