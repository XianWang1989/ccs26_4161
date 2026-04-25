
import os
import sys

# Adjust the path to include your appLib
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging output
print("Current Working Directory:", os.getcwd())
print("Sys Path:", sys.path)

# Importing modules
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code continues...
