
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    include_package_data=True,
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    # Optional: To specify scripts that will be installed
    entry_points={
        'console_scripts': [
            'mypackage=mypackage.mypackage:main',  # Adjust entry point as necessary
        ],
    },
)
