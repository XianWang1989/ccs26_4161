
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find the package structure
    py_modules=['plugin1', 'plugin2'],  # Include plugin1 and plugin2 as modules
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    zip_safe=False,
)
