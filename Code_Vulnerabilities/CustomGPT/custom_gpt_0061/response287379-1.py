
import os
import sys

# Adjust the path to include the appLib directory
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Check if the path is correctly added
print("Current PYTHONPATH:", sys.path)

# Now import modules
from tkinter import *
from SlotMapper import SlotMap  # This should now work if SlotMap is defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
