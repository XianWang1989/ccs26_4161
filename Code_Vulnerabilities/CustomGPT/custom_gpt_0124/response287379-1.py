
import os
import sys

# Assuming your structure is like this:
# current_directory/
# └── appLib/
#     ├── KB-GUI/
#     │   └── (other files)
#     └── SlotMapper.py

# Append paths to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debug print to check paths
print(sys.path)  # Ensure 'appLib' is in the path

# Import required modules
from tkinter import *
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"Import error: {e}")
