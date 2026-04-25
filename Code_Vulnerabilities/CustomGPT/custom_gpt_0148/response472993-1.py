
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    # Specify the entry points if needed
    entry_points={
        'myplugin': [
            'plugin1 = plugin1',
            'plugin2 = plugin2',
        ],
    },
    # Depending on your needs, you can add other metadata
    install_requires=[],  # Add your dependencies here
)
