
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # This automatically finds your package(s)
    include_package_data=True,  # Include files specified in MANIFEST.in
    package_data={
        'mypackage': ['*.py'],  # Include all .py files in the package
    },
    install_requires=[],  # Include any dependencies your package needs
)
