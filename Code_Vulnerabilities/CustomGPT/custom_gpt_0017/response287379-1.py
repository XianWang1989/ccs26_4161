
import os
import sys

# Assuming the following structure:
# appLib/
# ├── KB-GUI/
# │   └── your_gui_file.py
# ├── SlotMapper.py
# ├── ShelfTypeSelection.py
# ├── PackTypeSelection.py
# └── EntryWidgets.py

# Modify path to include appLib
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import modules
from tkinter import *
from SlotMapper import SlotMap       # Ensure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap
if __name__ == "__main__":
    root = Tk()
    slot_map = SlotMap()  # Ensure SlotMap is correctly instantiated
    root.mainloop()
