
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],
    install_requires=[],  # List any dependencies here
    zip_safe=False,  # Ensure that the package can be unzipped
)
