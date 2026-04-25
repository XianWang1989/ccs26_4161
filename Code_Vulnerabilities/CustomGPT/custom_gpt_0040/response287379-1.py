
import os
import sys

# Make sure to set the correct path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Sample usage of SlotMap
def main():
    slot_map_instance = SlotMap()
    print("SlotMap instance created")

if __name__ == "__main__":
    main()
