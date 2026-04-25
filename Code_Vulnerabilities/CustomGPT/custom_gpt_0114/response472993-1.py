
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    # Include your plugins in the package data
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include these plugins
    },
    # Other metadata
    author='Your Name',
    author_email='you@example.com',
    description='A sample Python package with plugins',
    long_description=open('README.txt').read(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
