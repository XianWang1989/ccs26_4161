
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],
    include_package_data=True,
    package_data={
        '': ['*.py'],  # This includes all .py files in the package
    },
    install_requires=[],
)
