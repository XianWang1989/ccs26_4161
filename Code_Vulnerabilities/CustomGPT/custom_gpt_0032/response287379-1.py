
import os
import sys

# Add the application library paths
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import necessary modules
from tkinter import *
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Error importing SlotMap: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your GUI code here
