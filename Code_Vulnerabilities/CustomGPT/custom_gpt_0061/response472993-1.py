
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include your plugins
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugin files in the package
    },
    include_package_data=True,
    install_requires=[],  # Add dependencies if needed
    entry_points={
        'console_scripts': [
            'mycommand=mypackage.mypackage:main',  # Change to your main function
        ],
    },
)
