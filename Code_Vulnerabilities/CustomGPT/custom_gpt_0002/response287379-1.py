
import os
import sys

# Correctly set the path to the 'appLib' directory.
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

from tkinter import *
# Ensure the SlotMapper is correctly named to avoid conflicts.
from appLib.KB_GUI.SlotMapper import SlotMap  
from appLib.KB_GUI.ShelfTypeSelection import ShelfTypeSelector
from appLib.KB_GUI.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.KB_GUI.EntryWidgets import EntryBase, ShelfSlotEntry
