
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # include standalone modules
    install_requires=[],  # list any dependencies your package requires
    package_data={
        'mypackage': ['*'],  # this will include all files in mypackage
    },
    entry_points={
        'console_scripts': [
            # You can add scripts if you have any
        ],
    },
    include_package_data=True,  # include all files specified in package_data
    zip_safe=False,  # set to False if you want to support .egg files
)
