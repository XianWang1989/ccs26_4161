
import os
import sys

# Updating sys.path correctly
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Debugging: Check current sys.path
print("Current PYTHONPATH:", sys.path)

# Ensure SlotMap is defined in SlotMapper
try:
    from SlotMapper import SlotMap  # or adjust path as necessary
except ImportError as e:
    print("ImportError:", e)

from tkinter import *

# Your remaining import statements
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
