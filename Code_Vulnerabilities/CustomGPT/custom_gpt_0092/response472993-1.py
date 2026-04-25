
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],
    include_package_data=True,  # This will include the plugins in the package
    install_requires=[],  # Add dependencies if needed
)
