
import os
import sys

# Ensure paths are correctly set
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Absolute import
from tkinter import *
from appLib.SlotMapper import SlotMap
from appLib.ShelfTypeSelection import ShelfTypeSelector
from appLib.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code continues here...
