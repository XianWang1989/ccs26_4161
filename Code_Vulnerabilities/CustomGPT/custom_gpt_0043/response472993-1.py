
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # This will automatically find your package
    package_data={
        # Include the plugins alongside the package
        '': ['plugin1.py', 'plugin2.py'],
    },
    include_package_data=True,
    # Other parameters as necessary
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python package with plugins',
    license='MIT',
    # Add any dependencies here, if needed
    install_requires=[
        # 'some_dependency',
    ],
)
