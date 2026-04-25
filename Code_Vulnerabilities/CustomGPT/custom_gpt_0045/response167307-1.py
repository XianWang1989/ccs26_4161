
import sys
import os

# Add custom source directories
sys.path.append('/path/to/your/source')
sys.path.append('/another/path/to/source')

# If you need to remove a directory
if '/path/to/remove' in sys.path:
    sys.path.remove('/path/to/remove')

# Verify the changes
print(sys.path)
