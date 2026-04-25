
import os
import sys

# Ensure the correct path
current_directory = os.getcwd()
app_lib_path = os.path.join(current_directory, 'appLib')

sys.path.append(app_lib_path)  # Ensure the main appLib is in the path
sys.path.append(os.path.join(app_lib_path, 'KB-GUI'))

# Import your modules
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is correctly defined in SlotMapper
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your code...
