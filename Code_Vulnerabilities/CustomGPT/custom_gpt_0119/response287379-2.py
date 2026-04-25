
import os
import sys

# Add appLib to your system path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMapper is recognized
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI application code goes here
