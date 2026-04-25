
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    # Specify the package directory where your plugin files are located
    package_data={
        'mypackage': ['plugin1.py', 'plugin2.py'],
    },
    # Additional metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A package that includes plugins',
    url='http://your.project.url',
)
