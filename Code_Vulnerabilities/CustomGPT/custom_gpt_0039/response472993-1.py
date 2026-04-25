
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Add any dependencies here
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in package
    },
    entry_points={
        'console_scripts': [
            'mycommand=mypackage.mypackage:main',  # Example entry point
        ],
    },
)
