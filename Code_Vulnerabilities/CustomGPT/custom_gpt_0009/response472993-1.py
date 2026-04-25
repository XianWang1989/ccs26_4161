
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],  # Specify your plugins here
    entry_points={
        'console_scripts': [
            'mypackage=mypackage.mypackage:main',  # if you have a main method
        ],
    },
)
