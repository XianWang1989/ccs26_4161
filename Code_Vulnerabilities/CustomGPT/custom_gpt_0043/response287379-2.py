
import os
import sys

# Assure that the sys.path is pointing correctly to your appLib and its relevant subdirectories
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *

# Adjust the import paths according to the hierarchy
from appLib.KB_GUI.SlotMapper import SlotMap
from appLib.KB_GUI.ShelfTypeSelection import ShelfTypeSelector
from appLib.KB_GUI.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.KB_GUI.EntryWidgets import EntryBase, ShelfSlotEntry

# Now you can use SlotMap and other classes/functions
