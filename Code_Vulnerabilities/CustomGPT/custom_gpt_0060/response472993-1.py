
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    description='A sample package with plugins',
    packages=find_packages(include=['mypackage', 'mypackage.*']),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],
    zip_safe=False,
)
