
import os
import sys

# Append the path to 'appLib' directory
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Ensure you check the structure of appLib
# For example, if SlotMapper.py is directly under appLib, use:
# from SlotMapper import SlotMap

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import Error: {e}")

# Proceed with other imports
from tkinter import *
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
