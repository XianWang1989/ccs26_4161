
# Assuming SlotMapper.py is located in 'appLib'
import os
import sys

# Adjust sys.path to include the appLib directory
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import the necessary components
from tkinter import *
from SlotMapper import SlotMap  # Make sure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap
def main():
    # Create an instance of SlotMap (ensure it's defined correctly inside SlotMapper)
    slot_map_instance = SlotMap()

    # Example GUI setup using tkinter
    root = Tk()
    root.title("Slot Mapper GUI")

    # Your GUI code here...

    root.mainloop()

if __name__ == '__main__':
    main()
