
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    # Include other files as well
    py_modules=['plugin1', 'plugin2'],
    include_package_data=True,
    package_data={
        '': ['*.py'],
    },
    # Define entry points if needed
    # entry_points={
    #     'console_scripts': [
    #         'your_command=mypackage.mypackage:main',
    #     ],
    # },
)
