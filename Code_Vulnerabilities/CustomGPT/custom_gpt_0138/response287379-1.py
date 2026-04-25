
import os
import sys

# Define the appLib directory
app_lib_path = os.path.join(os.getcwd(), 'appLib')

# Append paths
sys.path.append(os.path.join(app_lib_path, 'KB-GUI'))
sys.path.append(app_lib_path)

# Import necessary Tkinter components
from tkinter import *

# Attempt import of SlotMap explicitly from SlotMapper
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import failed: {e}")

# Continue with your remaining imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
