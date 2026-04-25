
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include the plugins in package directory
    },
    include_package_data=True,
    install_requires=[],  # Add any dependencies here
    description='A sample Python package with plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://example.com/mypackage',  # Replace with your package URL
)
