
import os
import sys

# Modify the PYTHONPATH to include the necessary directories
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_dir, 'appLib'))

from tkinter import *

# Use absolute import if SlotMapper is a module inside 'appLib'
from appLib.SlotMapper import SlotMap
from appLib.ShelfTypeSelection import ShelfTypeSelector
from appLib.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI logic here...
