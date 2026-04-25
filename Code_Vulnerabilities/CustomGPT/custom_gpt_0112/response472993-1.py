
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include plugins
    include_package_data=True,
    zip_safe=False,
    # Any other metadata can be added here
)
