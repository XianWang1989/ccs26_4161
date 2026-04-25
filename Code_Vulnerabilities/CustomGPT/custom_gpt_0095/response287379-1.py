
import os
import sys

# Append the paths to sys.path for imports
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import necessary modules
from tkinter import *
try:
    from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"Import Error: {e}")
