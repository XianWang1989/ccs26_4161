
import os
import sys

# Append correct paths
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Importing modules
from tkinter import *
# Use absolute imports
from appLib.SlotMapper import SlotMap
from appLib.ShelfTypeSelection import ShelfTypeSelector
from appLib.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code logic here
