
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # This will find the `mypackage` directory
    py_modules=['plugin1', 'plugin2'],  # Include plugin files
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        # Add other classifiers as needed
    ],
)
