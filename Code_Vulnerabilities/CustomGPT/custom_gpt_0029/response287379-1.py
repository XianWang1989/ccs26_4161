
import os
import sys

# Update sys.path to include the directory containing SlotMapper.py
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

try:
    from SlotMapper import SlotMap  # Attempt to import SlotMap again
except ImportError as e:
    print(f"ImportError: {e}")

# Proceed with other imports
from tkinter import *
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your application logic here
