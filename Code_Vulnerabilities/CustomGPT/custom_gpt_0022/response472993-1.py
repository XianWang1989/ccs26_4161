
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include your plugins here
    include_package_data=True,
    install_requires=[],  # List your dependencies here
    entry_points={
        'console_scripts': [
            'mycommand=mypackage:mypackage_function',  # Example entry point
        ],
    },
)
