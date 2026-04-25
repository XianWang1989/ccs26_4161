
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # This will include non-Python files
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    zip_safe=False,
)
