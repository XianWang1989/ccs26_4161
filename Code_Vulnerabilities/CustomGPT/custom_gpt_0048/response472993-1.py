
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    include_package_data=True,
    install_requires=[],
    python_requires='>=2.7',
)
