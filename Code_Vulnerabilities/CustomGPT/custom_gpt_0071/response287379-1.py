
import os
import sys

# Print sys.path for debugging
print("Current PYTHONPATH:", sys.path)

# Update PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Now import your modules
from tkinter import *
# Ensure SlotMapper.py is in the correct directory
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
