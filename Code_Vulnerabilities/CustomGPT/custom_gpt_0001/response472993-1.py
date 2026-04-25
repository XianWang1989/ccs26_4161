
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        # Include plugin files with your package
        'mypackage': ['../plugin1.py', '../plugin2.py'],
    },
    include_package_data=True,
    description='My package with plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://example.com/mypackage',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
