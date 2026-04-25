
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include these files
    },
    install_requires=[
        # Add your package dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python package with plugins',
    url='https://github.com/yourusername/mypackage',  # Your GitHub or project link
)
