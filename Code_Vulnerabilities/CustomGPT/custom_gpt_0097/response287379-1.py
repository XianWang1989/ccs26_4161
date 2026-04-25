
import os
import sys

# Adding paths to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging path
print("Current sys.path:", sys.path)

# Check if SlotMap exists in SlotMapper
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)

# Other imports
from tkinter import *
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
