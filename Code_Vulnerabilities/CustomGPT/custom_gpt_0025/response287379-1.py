
import os
import sys

# Set up the appLib path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
if app_lib_path not in sys.path:
    sys.path.append(app_lib_path)

# Set the path for the GUI
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')
if kb_gui_path not in sys.path:
    sys.path.append(kb_gui_path)

# Verify if paths are set correctly
print("Current sys.path entries:")
for path in sys.path:
    print(path)

# Import required modules
from tkinter import *
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import error: {e}")
    raise

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
