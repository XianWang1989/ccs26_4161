
import os
import sys

# Adding the appLib path to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging to print sys.path and check
print("Current sys.path:", sys.path)

from KB_GUI.SlotMapper import SlotMap  # Use absolute import
from KB_GUI.ShelfTypeSelection import ShelfTypeSelector
from KB_GUI.PackTypeSelection import PackTypeSlotMappingSelector
from KB_GUI.EntryWidgets import EntryBase, ShelfSlotEntry

# Check for SlotMap class
print("SlotMap:", SlotMap)
