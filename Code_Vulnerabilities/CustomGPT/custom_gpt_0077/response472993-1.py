
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    description='A sample Python package with plugins',
    packages=find_packages(),  # This will include mypackage
    py_modules=['plugin1', 'plugin2'],  # Include your plugins
    install_requires=[],  # Add your dependencies here
    package_data={
        '': ['*.py'],  # Include all Python files
    },
    include_package_data=True,
    zip_safe=False,
)
