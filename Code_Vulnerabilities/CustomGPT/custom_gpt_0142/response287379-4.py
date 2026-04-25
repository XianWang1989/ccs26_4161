
import os
import sys

# Ensure the path is pointing to your appLib
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

from tkinter import *

# Adjust imports based on actual file location if necessary
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your main GUI code here
