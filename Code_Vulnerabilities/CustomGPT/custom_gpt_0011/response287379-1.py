
import os
import sys

# Modify PYTHONPATH
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)
print("Current PYTHONPATH:", sys.path)

# Try importing SlotMap
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)

# Continue with other imports
from tkinter import *
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
