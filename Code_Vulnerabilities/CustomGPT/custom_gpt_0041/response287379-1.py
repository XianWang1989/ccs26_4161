
import os
import sys

# Add directories to sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')
sys.path.append(kb_gui_path)
sys.path.append(app_lib_path)

# Debugging: Check sys.path contents
print("Current PYTHONPATH:", sys.path)

from tkinter import *

# Attempting to import SlotMap
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError occurred:", e)

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Continue with your GUI code...
