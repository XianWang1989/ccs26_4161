
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include the plugins as separate modules
    description='A sample Python package with plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/mypackage',  # Add your package URL
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
