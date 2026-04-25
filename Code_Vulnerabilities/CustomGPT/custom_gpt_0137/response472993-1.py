
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    packages=find_packages(),  # This will include __init__.py files
    py_modules=['plugin1', 'plugin2'],  # Include your plugin modules
    include_package_data=True,
    zip_safe=False,
    description='My Sample Package with Plugins',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/mypackage',  # Update with your repository
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',  # Also support Python 3 if needed
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Change to your license
    ],
)

# Note that you'd need to run the setup script with the command:
# python setup.py install
