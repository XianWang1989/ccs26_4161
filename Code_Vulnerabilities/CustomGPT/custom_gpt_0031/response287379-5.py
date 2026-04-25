
import os
import sys

# Define paths
app_lib_path = os.path.join(os.getcwd(), 'appLib')
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')

# Append paths to sys.path
sys.path.append(kb_gui_path)
sys.path.append(app_lib_path)

# Debug the sys.path
print(sys.path)

# Import necessary modules
from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
