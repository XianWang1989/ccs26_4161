
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically include packages from mypackage
    include_package_data=True,
    package_data={
        'mypackage': ['*.py', '../plugin1.py', '../plugin2.py'],  # Include plugins
    },
    install_requires=[
        # List your package dependencies here (if any)
    ],
    # Optional: Additional metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python package with plugins.',
    url='http://your.package.url',
)

