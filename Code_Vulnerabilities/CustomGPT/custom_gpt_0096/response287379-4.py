
import os
import sys

# Append the appLib directory
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Check if the path was appended correctly
print(sys.path)

from tkinter import *
# Attempt importing SlotMap using the correct path
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import Error: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
