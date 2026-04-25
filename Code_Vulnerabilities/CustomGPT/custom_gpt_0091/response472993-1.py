
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['plugin1', 'plugin2'],
    install_requires=[],  # Add any dependencies your package needs
    package_data={
        '': ['*.py'],  # Include all Python files
    },
    entry_points={  # Define entry points if needed
        # 'console_scripts': [
        #     'myscript=mypackage:mypackage_function',
        # ]
    },
)
