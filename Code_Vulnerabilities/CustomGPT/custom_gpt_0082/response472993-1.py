
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # This will include your plugins
    py_modules=['plugin1', 'plugin2'],  # List your plugin modules
    install_requires=[],  # List any dependencies your package needs
    package_data={
        # Include the plugins in the package installation
        '': ['*.py'],  # Include all Python files
    },
    entry_points={
        'console_scripts': [
            # Create command line scripts if needed
            # 'some_command = mypackage.mypackage:main',
        ],
    },
)
