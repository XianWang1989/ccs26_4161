
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # Include non-package files
    py_modules=['plugin1', 'plugin2'],  # Include the plugin modules
    install_requires=[],  # List any dependencies here
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Specify plugins to include
    },
)
