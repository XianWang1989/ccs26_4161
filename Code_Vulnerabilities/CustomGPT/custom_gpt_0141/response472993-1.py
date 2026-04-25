
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically find packages in mypackage/
    package_data={
        '': ['*.py'],  # Include all .py files in the package
    },
    include_package_data=True,
    # Include the external plugin files
    py_modules=['plugin1', 'plugin2'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
)
