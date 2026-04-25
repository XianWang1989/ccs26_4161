
import os
import sys

# Add the directories to sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
gui_path = os.path.join(app_lib_path, 'KB-GUI')

sys.path.append(gui_path)
sys.path.append(app_lib_path)

# Optional: Clear the import cache for troubleshooting
import importlib
import SlotMapper
importlib.reload(SlotMapper)

# Import the necessary modules
from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Sample usage of SlotMap
def use_slot_map():
    my_slot_map = SlotMap()  # Make sure SlotMap is initialized correctly
    # Do something with my_slot_map

if __name__ == "__main__":
    use_slot_map()
