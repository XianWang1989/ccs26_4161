
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # This will find `mypackage`
    py_modules=['plugin1', 'plugin2'],  # Include your plugins
    include_package_data=True,
    description='A sample package with plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://yourpackageurl.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.x',
    ],
)
