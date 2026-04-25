
import os
import sys

# Append the correct paths
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *

# Now import SlotMap
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Sample code to initialize your Tkinter app
root = Tk()
slot_map = SlotMap()  # Create an instance of SlotMap

# Add more GUI functionalities as needed
root.mainloop()
