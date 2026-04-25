
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # Include other files like plugins
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the root
    },
    zip_safe=False,  # Set to False to keep directory structure intact
)
