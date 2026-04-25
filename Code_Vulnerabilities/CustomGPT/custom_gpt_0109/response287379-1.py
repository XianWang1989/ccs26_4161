
import os
import sys

# Add the necessary directories to sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
app_gui_path = os.path.join(app_lib_path, 'KB-GUI')

sys.path.append(app_lib_path)
sys.path.append(app_gui_path)

# Try importing here
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import Error: {e}")

from tkinter import *
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
