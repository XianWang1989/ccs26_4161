
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # This will include non-Python files specified
    py_modules=['plugin1', 'plugin2'],  # Specify the plugin files directly
    entry_points={
        'console_scripts': [
            # If you want to create any CLI commands, they can be added here
        ],
    },
    # Include all your data files
    package_data={
        '': ['*.py'],  # Include all Python files
    },
)
