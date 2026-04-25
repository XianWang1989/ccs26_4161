
import os
import sys

# Update sys.path correctly
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)
sys.path.append(os.path.join(app_lib_path, 'KB-GUI'))

# Check to ensure paths are correctly appended
print("Current sys.path:", sys.path)

from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
