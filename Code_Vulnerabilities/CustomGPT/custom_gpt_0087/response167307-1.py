
import sys
import os

# Example directories
production_dir = "/path/to/production"
testing_dir = "/path/to/testing"
git_submodule_dir = "/path/to/git/submodule"

# Add directories to PYTHONPATH
sys.path.append(production_dir)
sys.path.append(testing_dir)
sys.path.append(git_submodule_dir)

# Verify the changes
print(sys.path)
