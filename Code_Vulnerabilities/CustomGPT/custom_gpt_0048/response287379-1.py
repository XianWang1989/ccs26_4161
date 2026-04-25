
import os
import sys

# Ensure the path is correctly set
sys.path.append(os.path.join(os.getcwd(), 'appLib'))  # adjusting the path for SlotMapper

from tkinter import *

# Import your modules
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Error importing SlotMap: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
