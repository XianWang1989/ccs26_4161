
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include your plugins
    package_data={
        '': ['*.py'],  # Ensure .py files are included
    },
    include_package_data=True,
    install_requires=[],  # Add any dependencies your package needs
)
