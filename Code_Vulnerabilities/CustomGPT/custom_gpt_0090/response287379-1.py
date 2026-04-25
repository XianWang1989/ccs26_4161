
import os
import sys

# Adding directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Verify the path is correct
print(sys.path)

# Importing modules
from tkinter import *
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError occurred: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
