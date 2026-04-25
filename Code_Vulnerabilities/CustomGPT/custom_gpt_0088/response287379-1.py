
import os
import sys

# Append paths to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import necessary modules
from tkinter import *

# Make sure SlotMapper.py is in the correct path
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your main GUI code goes here
if __name__ == "__main__":
    root = Tk()
    # Initialize your GUI components
    root.mainloop()
