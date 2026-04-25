
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Add your plugins here
    include_package_data=True,
    install_requires=[],  # Add any dependencies your package needs
    entry_points={
        'console_scripts': [
            'run-plugin1 = plugin1:main',  # Assuming plugin1 has a main function
            'run-plugin2 = plugin2:main',  # Assuming plugin2 has a main function
        ],
    },
)
