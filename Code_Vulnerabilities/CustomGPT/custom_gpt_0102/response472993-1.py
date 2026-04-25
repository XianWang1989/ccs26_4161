
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files
    py_modules=['plugin1', 'plugin2'],  # Register plugin modules
    install_requires=[],  # Add any dependencies here
    entry_points={
        'console_scripts': [
            'your_command=mypackage.mypackage:main'  # if you have a main function to run
        ],
    },
)
