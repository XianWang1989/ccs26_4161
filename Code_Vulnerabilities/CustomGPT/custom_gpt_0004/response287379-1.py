
import os
import sys

# Define the base directory
base_dir = os.getcwd()
# Append the correct directories to sys.path
sys.path.append(os.path.join(base_dir, 'appLib', 'KB-GUI'))  # For GUI specific imports
sys.path.append(os.path.join(base_dir, 'appLib'))  # For SlotMapper

# Importing modules after appending the paths
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap
if __name__ == "__main__":
    # Initialize your GUI or main application logic here
    root = Tk()
    slot_map_instance = SlotMap()  # Assuming SlotMap is a class
    # Your GUI code here...
    root.mainloop()
