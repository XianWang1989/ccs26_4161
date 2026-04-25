
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'mypackage': ['plugins/*.py'],  # Include all plugins
    },
    entry_points={
        'console_scripts': [
            'mycommand=mypackage.mypackage:main_function',  # Replace with your command
        ],
    },
)
