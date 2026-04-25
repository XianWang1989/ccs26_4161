
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['plugin1.py', 'plugin2.py'],
    },
    include_package_data=True,
    zip_safe=False,
)
