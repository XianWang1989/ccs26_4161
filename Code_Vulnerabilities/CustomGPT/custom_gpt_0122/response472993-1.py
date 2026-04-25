
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically includes mypackage
    py_modules=['plugin1', 'plugin2'],  # Include standalone modules
    include_package_data=True,
    zip_safe=False,  # Optional, depending on your needs
    description='A package with plugins',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
