
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],
    include_package_data=True,
    package_data={
        '': ['plugin1.py', 'plugin2.py'],
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)
