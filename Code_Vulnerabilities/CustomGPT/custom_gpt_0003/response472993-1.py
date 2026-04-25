
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],  # Listing the plugin modules
    # Alternatively, you can add data files directly as well.
    # data_files=[('mypackage', ['plugin1.py', 'plugin2.py'])],
    install_requires=[
        # List any dependencies your package requires
    ],
    entry_points={
        # If you have any command line tools related to your package, define them here
    }
)
