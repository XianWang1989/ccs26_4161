
import sys
import os

# Add multiple directories to PYTHONPATH
project_root = '/path/to/your/project'
test_dir = '/path/to/your/tests'
submodule_dir = '/path/to/your/submodule'

# Update sys.path to include the desired directories
sys.path.append(project_root)
sys.path.append(test_dir)
sys.path.append(submodule_dir)

# Verify the directories were added
print(sys.path)
