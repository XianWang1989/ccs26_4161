
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    packages=['mypackage'],
    py_modules=['plugin1', 'plugin2'],  # Include plugin files
    zip_safe=False,  # Optional: makes it easier for plugins to load
    description='A sample package with plugins',
    long_description=open('README.md').read(),  # If you have a README
    install_requires=[],  # List any dependencies here
)
