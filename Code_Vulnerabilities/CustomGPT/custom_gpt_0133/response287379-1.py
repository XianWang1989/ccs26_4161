
import os
import sys

# Append the directories containing your modules to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
# You might also want to append the 'appLib' directory if another module depends on it
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import necessary classes or functions
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Now you can use these imported classes/functions
