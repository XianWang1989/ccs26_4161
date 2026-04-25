
import os
import sys

# Add directories to PYTHONPATH
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Import only after modifying sys.path
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Sample code to show how to use SlotMap
def main():
    print("Using SlotMap from SlotMapper")
    slot_map = SlotMap()  # Ensure SlotMap is initialized properly

if __name__ == "__main__":
    main()
