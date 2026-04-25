
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['plugin1.py', 'plugin2.py'],
    },
    zip_safe=False,
    install_requires=[],
)
