
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # include plugins in the package
    },
    include_package_data=True,
    install_requires=[],  # specify any dependencies your package needs
    description='A sample Python package with plugins.',
)
