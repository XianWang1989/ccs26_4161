
# SlotMapper.py
class SlotMap:
    def __init__(self):
        print("SlotMap initialized")

# Your main Script
import os
import sys

# Adjust the path correctly
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Ensure that 'SlotMapper.py' is in the directory you're importing from
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import error: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage
slot_map_instance = SlotMap()
