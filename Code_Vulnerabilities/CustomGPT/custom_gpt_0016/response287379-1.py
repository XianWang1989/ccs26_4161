
import os
import sys

# Define the path to appLib and KB-GUI
app_lib_path = os.path.join(os.getcwd(), 'appLib')
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')

# Append the paths to sys.path
sys.path.append(app_lib_path)
sys.path.append(kb_gui_path)

# Import necessary modules
from tkinter import *
from SlotMapper import SlotMap  # Assuming SlotMap is defined in this file
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap
slot_map = SlotMap()  # Initialize SlotMap if it has an __init__ method
