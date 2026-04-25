
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # To include additional files like your plugins
    py_modules=['plugin1', 'plugin2'],
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add any console scripts here
        ],
    },
)
