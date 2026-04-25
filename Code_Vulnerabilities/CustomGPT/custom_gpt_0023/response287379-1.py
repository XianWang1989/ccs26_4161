
import os
import sys

# Set the path to the appLib directory
lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(lib_path)

# Import your modules
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined correctly
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
