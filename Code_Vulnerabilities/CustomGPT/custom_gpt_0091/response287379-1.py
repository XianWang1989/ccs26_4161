
import os
import sys

# Adding appLib to the system path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Check if SlotMapper module is being imported correctly
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import error: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
