
import os
import sys

# Add the relevant paths to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Import modules
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")
    print("Check if SlotMapper.py is in the correct directory and the name is correct.")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
