
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # To include non-Python files
    py_modules=['plugin1', 'plugin2'],  # Register your plugins
    package_data={
        '': ['*.py'],  # Include all Python files
    },
    install_requires=[],  # Add your dependencies here
)
