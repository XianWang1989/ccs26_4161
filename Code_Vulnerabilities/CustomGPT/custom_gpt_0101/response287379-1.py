
import os
import sys

# Adding the appLib directory to the system path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Verify the updated system path
print(sys.path)

from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap if successfully imported
def create_slot():
    slot = SlotMap()  # Assuming SlotMap is a callable class or function
    print(slot)

if __name__ == "__main__":
    create_slot()
