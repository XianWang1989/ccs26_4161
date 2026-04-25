
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins at package level
    },
    install_requires=[],  # List your package dependencies here
)
