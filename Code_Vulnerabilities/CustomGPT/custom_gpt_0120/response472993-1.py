
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    package_data={
        '': ['plugin1.py', 'plugin2.py'],
    },
    entry_points={
        'console_scripts': [
            'mypackage=mypackage.mypackage:main',  # Adjust if you have a main function
        ],
    },
)
