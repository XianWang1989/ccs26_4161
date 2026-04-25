
import os
import sys

# Ensure correct path to 'appLib'
current_dir = os.getcwd()
app_lib_dir = os.path.join(current_dir, 'appLib', 'KB-GUI')

sys.path.append(app_lib_dir)
sys.path.append(os.path.join(current_dir, 'appLib'))

# Importing modules after adjusting the path
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Debugging print to verify paths
print("Current sys.path:")
for path in sys.path:
    print(path)
