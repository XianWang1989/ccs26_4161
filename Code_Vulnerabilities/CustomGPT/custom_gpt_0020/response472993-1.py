
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # This includes the files specified in MANIFEST.in
    package_data={
        'mypackage': ['*.py'],  # Include all Python files within the package
    },
    # Optional dependencies (if any)
    install_requires=[],
)

