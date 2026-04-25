
import sys
import os

# Add directories to PYTHONPATH
project_root = os.path.abspath('path/to/your/project')
test_root = os.path.abspath('path/to/your/test')
sys.path.append(project_root)
sys.path.append(test_root)

# Verify paths are added
print("Current PYTHONPATH:", sys.path)
