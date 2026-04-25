
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include your plugins as separate modules
    install_requires=[],  # Add any package dependencies here
    package_data={
        '': ['*.py'],  # Include all Python files
    },
    include_package_data=True,
)
