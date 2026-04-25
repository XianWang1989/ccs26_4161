from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # This includes plugin1.py and plugin2.py
    include_package_data=True,
)
