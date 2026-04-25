
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,  # Include non-code files
    package_data={
        '': ['plugin1.py', 'plugin2.py'],  # Include your plugins
    },
    zip_safe=False,  # Ensure it is not zipped
    entry_points={  # Optional: Define entry points for plugins if needed
        'console_scripts': [
            'my-script=mypackage.mypackage:main',  # Example entry point
        ],
    },
)
