
import os
import sys

# Update the paths to include your appLib directories
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import your modules
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap, assuming it’s a class
def main():
    window = Tk()
    slot_map_instance = SlotMap()  # Create instance of SlotMap
    # Your GUI logic goes here
    window.mainloop()

if __name__ == "__main__":
    main()
