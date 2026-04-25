
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include your plugins
    install_requires=[],  # List your dependencies here
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins in the package
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',  # Adjust for your Python version
        'License :: OSI Approved :: MIT License',  # Adjust license if necessary
    ],
)
