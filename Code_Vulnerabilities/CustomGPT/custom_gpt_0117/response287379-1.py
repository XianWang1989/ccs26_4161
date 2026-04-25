
# Directory Structure
# ├── appLib
# │   ├── __init__.py
# │   ├── SlotMapper.py
# │   ├── ShelfTypeSelection.py
# │   ├── PackTypeSelection.py
# │   ├── EntryWidgets.py
# └── main.py

# SlotMapper.py
class SlotMap:
    def __init__(self):
        print("SlotMap initialized.")

# main.py
import os
import sys

# Adjusting sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging - check sys.path
print("Current sys.path:", sys.path)

# Imports
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMapper.py is in appLib
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage
if __name__ == "__main__":
    root = Tk()
    slot_map_instance = SlotMap()
    root.mainloop()
