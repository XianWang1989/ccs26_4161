
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    scripts=['plugin1.py', 'plugin2.py'],
    zip_safe=False,  # Optional: allows plugins to be accessible as scripts
)
