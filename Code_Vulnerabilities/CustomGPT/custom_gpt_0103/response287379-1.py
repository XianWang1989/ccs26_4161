
import os
import sys

# Ensure you append paths correctly
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Print sys.path to debug
print("Current sys.path:")
for p in sys.path:
    print(p)

from tkinter import *

# Import SlotMap after all paths are set
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI logic here
