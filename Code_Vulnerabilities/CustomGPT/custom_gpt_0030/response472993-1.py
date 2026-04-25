
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    install_requires=[],  # List your package dependencies here
    entry_points={       # Optional: specify entry points if needed
        'console_scripts': [
            'mypackage=mypackage.mypackage:main',  # Change this as per your entry point
        ]
    },
)
