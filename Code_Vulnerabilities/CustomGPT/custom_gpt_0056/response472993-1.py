
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],
    install_requires=[],  # Add your project dependencies here
    package_data={
        '': ['*.py'],  # Include all Python files in the package
    },
    entry_points={
        'console_scripts': [
            # Define any console scripts here if needed
        ],
    },
)
