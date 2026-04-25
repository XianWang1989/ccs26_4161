
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],
    install_requires=[],
    include_package_data=True,

    # Adjust this if you're using a different Python version
    python_requires='>=2.7', 

    # Metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python package with plugins.',
    url='https://github.com/yourusername/mypackage',  # Your project's URL
)
