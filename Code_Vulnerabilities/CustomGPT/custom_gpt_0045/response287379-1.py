
import os
import sys

# Update the PYTHONPATH to include the necessary directories
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import the necessary modules
from tkinter import *

# Import the SlotMap class from SlotMapper
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Error importing SlotMap: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
