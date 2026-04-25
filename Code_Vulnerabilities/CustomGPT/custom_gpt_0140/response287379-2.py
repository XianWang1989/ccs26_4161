
import os
import sys

# Adding the necessary paths
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Optional: Print sys.path for debugging
print(sys.path)

# Import the necessary modules
from tkinter import *
# Add this import to ensure SlotMapper is correctly referenced
import SlotMapper

# Check if SlotMap is accessible after importing SlotMapper
if hasattr(SlotMapper, 'SlotMap'):
    SlotMap = SlotMapper.SlotMap
else:
    raise ImportError("SlotMap not found in SlotMapper")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
