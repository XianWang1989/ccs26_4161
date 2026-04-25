
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],
    install_requires=[],  # Add your dependencies here
    entry_points={
        'console_scripts': [
            'myscript=mypackage.mypackage:main',  # Adjust as needed
        ]
    },
)
