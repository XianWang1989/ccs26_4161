
import os
import sys

# Assuming your script is in the `TEC-KB` folder
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Import the necessary modules
from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code here
def main():
    root = Tk()
    # Example usage of SlotMap, ShelfTypeSelector, etc.
    # Your GUI setup...

    root.mainloop()

if __name__ == "__main__":
    main()
