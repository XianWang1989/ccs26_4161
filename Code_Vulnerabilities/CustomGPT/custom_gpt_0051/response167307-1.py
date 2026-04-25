
import sys
import os

# Specify the directories you want to add
src_dirs = [
    '/path/to/production_code',
    '/path/to/testing_code',
    '/path/to/git_submodule',
]

# Add each directory to sys.path
for src_dir in src_dirs:
    if os.path.exists(src_dir):
        sys.path.append(src_dir)

# Now you can import modules from these directories
