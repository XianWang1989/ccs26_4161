
import os
import sys

# Ensure to append the correct directory
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import error: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Verification print
print("Modules imported successfully.")
