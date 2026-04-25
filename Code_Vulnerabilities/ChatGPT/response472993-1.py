
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically finds mypackage/ and includes it
    py_modules=['plugin1', 'plugin2'],  # Include standalone plugins
    install_requires=[],  # Add any external dependencies your package needs
    include_package_data=True,  # Include data files based on MANIFEST.in if present
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify supported Python versions
        'License :: OSI Approved :: MIT License', 
    ],
)
