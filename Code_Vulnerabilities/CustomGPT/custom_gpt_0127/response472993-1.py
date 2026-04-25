
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find mypackage
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    py_modules=['plugin1', 'plugin2'],
    install_requires=[],  # Specify any dependencies your package has
)
