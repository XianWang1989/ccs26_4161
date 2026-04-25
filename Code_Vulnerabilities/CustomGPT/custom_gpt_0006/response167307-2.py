
import sys

# List of directories to add
paths_to_add = [
    "/path/to/production",
    "/path/to/testing",
    "/path/to/git_submodule"
]

for path in paths_to_add:
    if path not in sys.path:
        sys.path.append(path)

# Import modules from the added directories
import production_module
import testing_module
