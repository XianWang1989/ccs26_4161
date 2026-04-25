
import os
import sys

# Ensure the appLib path is correctly set
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging: Print the current sys.path to ensure the paths are included
print("Current sys.path:", sys.path)

from tkinter import *

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Placeholder for other imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap if successfully imported
if 'SlotMap' in locals():
    slot_map_instance = SlotMap()
    print("SlotMap was imported successfully!")
else:
    print("SlotMap could not be imported.")
