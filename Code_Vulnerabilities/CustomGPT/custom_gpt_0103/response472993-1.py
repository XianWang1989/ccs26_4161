
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['plugin1', 'plugin2'],  # Include your plugins as modules
    package_data={
        '': ['*.py'],  # Include all .py files
    },
    include_package_data=True,
    install_requires=[  # Any dependencies your package may have
        # 'some_dependency',
    ],
)
