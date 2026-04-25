
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],
    include_package_data=True,
    install_requires=[],  # Add your requirements here
    entry_points={
        'console_scripts': [
            'mycommand=mypackage.mypackage:main',  # Update with your entry point
        ],
    },
)
