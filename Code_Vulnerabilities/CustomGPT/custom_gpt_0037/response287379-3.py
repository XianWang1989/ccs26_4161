
import os
import sys

# Adding the directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code goes here
def main():
    root = Tk()
    # Example usage of SlotMap
    slot_map_instance = SlotMap()
    # Setup your GUI components
    root.mainloop()

if __name__ == "__main__":
    main()
