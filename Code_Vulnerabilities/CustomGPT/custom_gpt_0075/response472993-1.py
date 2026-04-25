
from setuptools import setup, find_packages

# Define the required metadata
setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugin files
    },
    include_package_data=True,
    install_requires=[],
    description='A sample package with plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://example.com/mypackage',
)
