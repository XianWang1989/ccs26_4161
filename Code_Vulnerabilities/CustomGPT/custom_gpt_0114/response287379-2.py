
# Directory structure:
# appLib/
# ├── __init__.py
# ├── SlotMapper.py
# ├── ShelfTypeSelection.py
# ├── PackTypeSelection.py
# └── EntryWidgets.py
# gui.py

# gui.py
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Sample usage
if __name__ == "__main__":
    root = Tk()
    slot_map = SlotMap()  # Create instance of SlotMap
    # Add your GUI setup code here
    root.mainloop()
