
import os
import sys

# Specify the paths for the appLib and its subfolders
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Attempt to import necessary modules
try:
    from SlotMapper import SlotMap  # Ensure SlotMap exists in SlotMapper.py
except ImportError as e:
    print(f"Import error: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code here...
