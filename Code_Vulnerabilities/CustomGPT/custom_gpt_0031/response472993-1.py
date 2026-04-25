
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # Automatically finds packages in the mypackage directory
    include_package_data=True,  # Include other files specified in MANIFEST.in
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include plugins at the root level
    },
    entry_points={
        'console_scripts': [
            # Define any console scripts if needed
        ],
    },
)
