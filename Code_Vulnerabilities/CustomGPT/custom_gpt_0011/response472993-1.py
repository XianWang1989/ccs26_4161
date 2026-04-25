
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # This tells setuptools to include these modules
    include_package_data=True,
    package_data={
        '': ['*.py'],  # Include all .py files
    },
    zip_safe=False,  # This is useful if you want to modify the package after it is installed
)
