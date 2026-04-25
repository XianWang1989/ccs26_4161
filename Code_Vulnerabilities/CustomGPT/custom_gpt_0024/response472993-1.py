
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # Include the plugin files
        '': ['plugin1.py', 'plugin2.py'],
    },
    # Optional: specify install_requires for any dependencies
    install_requires=[
        # Add any package dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package with plugins.',
    zip_safe=False,  # Set to False if the package requires directory structure
)
