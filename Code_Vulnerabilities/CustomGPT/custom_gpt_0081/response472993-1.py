
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find package and sub-packages
    include_package_data=True,  # Include the files specified in MANIFEST.in
    package_data={
        'mypackage.plugins': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    install_requires=[],  # List dependencies here
)
