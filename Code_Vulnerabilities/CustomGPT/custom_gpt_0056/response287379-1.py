
import os
import sys

# Add the directory containing SlotMapper.py
app_lib_path = os.path.join(os.getcwd(), 'appLib')
if app_lib_path not in sys.path:
    sys.path.append(app_lib_path)

# Check if the KB-GUI subdirectory is required
gui_path = os.path.join(app_lib_path, 'KB-GUI')
if gui_path not in sys.path:
    sys.path.append(gui_path)

# Now, import necessary modules
from tkinter import *

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
