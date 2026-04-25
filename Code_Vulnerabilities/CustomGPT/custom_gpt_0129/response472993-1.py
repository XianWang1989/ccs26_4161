
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        # Specify the package data to include the plugins
        'mypackage': [
            '../plugin1.py',
            '../plugin2.py',
        ],
    },
    include_package_data=True,
    description='A sample Python package with plugins.',
    author='Your Name',
    author_email='youremail@example.com',
    url='http://yourpackagehomepage.com', # Optional
)
