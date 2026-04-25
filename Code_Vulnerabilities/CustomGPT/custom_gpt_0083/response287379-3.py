
# Your main script
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

from tkinter import *
from appLib.KB_GUI.SlotMapper import SlotMap  # Absolute import

# Other imports
from appLib.KB_GUI.ShelfTypeSelection import ShelfTypeSelector
from appLib.KB_GUI.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.KB_GUI.EntryWidgets import EntryBase, ShelfSlotEntry

# Your application logic here
