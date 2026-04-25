
import os
import sys

# Append directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print("Current sys.path:", sys.path)  # Debugging line to check the PYTHONPATH

try:
    from SlotMapper import SlotMap  # Attempt to import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")  # Catch import errors and display

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your code here...
