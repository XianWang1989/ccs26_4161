
import os
import sys

# Add the appLib directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import necessary modules
from tkinter import *
# Importing SlotMap from SlotMapper
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")
    print("Ensure that SlotMapper.py is in the correct directory and SlotMap is defined.")
    raise

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your code logic...
