
import os
import sys

# Add directories to path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import statements
from tkinter import *
from appLib.SlotMapper import SlotMap  # Adjust the path if necessary
from appLib.ShelfTypeSelection import ShelfTypeSelector
from appLib.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.EntryWidgets import EntryBase, ShelfSlotEntry
