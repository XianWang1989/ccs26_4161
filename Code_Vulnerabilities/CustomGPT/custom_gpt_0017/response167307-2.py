
import sys

# Adding multiple directories dynamically
source_dirs = [
    '/path/to/prod_code',
    '/path/to/test_code',
    '/path/to/git_submodule/python_packages'
]

for dir in source_dirs:
    if dir not in sys.path:
        sys.path.append(dir)

# Now you can import your modules
import prod_module
import test_module
