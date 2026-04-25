
import os
import sys

# Append directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *

# Import the SlotMapper module
import SlotMapper
SlotMap = SlotMapper.SlotMap  # Access SlotMap from the imported module

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI setup code can go here
