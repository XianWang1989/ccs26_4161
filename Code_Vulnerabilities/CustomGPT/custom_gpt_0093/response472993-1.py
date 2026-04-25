
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    description='My Example Python Package',
    author='Your Name',
    author_email='your.email@example.com',
    include_package_data=True,
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the egg package
    },
)
