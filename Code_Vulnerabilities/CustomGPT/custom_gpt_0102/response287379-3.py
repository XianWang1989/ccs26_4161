
import os
import sys

# Adjust the path where SlotMapper is located
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Example imports
from SlotMapper import SlotMap  # Ensure SlotMap is properly defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your main application code here
