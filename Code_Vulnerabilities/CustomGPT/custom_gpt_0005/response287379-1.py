
import os
import sys

# Add the correct directory containing SlotMapper.py
current_directory = os.getcwd()
app_lib_path = os.path.join(current_directory, 'appLib')
sys.path.append(app_lib_path)

# Import necessary modules
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMapper.py exists here
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
