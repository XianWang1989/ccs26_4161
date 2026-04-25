
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugin files
    },
    install_requires=[],  # Add any dependencies here
    # Additional metadata
    author='Your Name',
    author_email='youremail@example.com',
    description='A package with plugins',
    url='http://example.com/mypackage',  # Update with your package URL
)
