
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # To include non-package files
    py_modules=['plugin1', 'plugin2'],  # Include plugins as modules
    install_requires=[],  # List your dependencies here
    entry_points={
        'console_scripts': [
            # Add console scripts if needed
        ],
    },
)
