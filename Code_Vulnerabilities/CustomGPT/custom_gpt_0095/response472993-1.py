
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],  # List your plugin modules here
    install_requires=[],  # Add any dependencies your package needs
    zip_safe=False,  # Allows the package to be unzipped during use
)
