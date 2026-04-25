
import os
import sys

# Adjusting the path to ensure SlotMapper can be found
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *
# Use an absolute import from your module path if necessary
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap (assuming it's a class)
if __name__ == "__main__":
    slot_map_instance = SlotMap()  # Initialize your SlotMap instance
    # Continue with the rest of your application
