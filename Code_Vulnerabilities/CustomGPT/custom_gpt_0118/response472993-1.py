
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'mypackage': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    include_package_data=True,
    install_requires=[],  # Add your project dependencies here
    entry_points={
        'console_scripts': [
            # Entry points can be defined here if you have command line scripts
        ],
    },
)
