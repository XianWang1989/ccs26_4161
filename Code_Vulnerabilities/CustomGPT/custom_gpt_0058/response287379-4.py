
import os
import sys

# Add paths to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging output
print("Current sys.path:", sys.path)

from tkinter import *
# Ensure SlotMapper has SlotMap defined
from SlotMapper import SlotMap  # Check if SlotMap is correctly defined in SlotMapper
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# The rest of your code using these imports
