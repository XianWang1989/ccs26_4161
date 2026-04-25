
import os
import sys

# Get the current working directory
current_dir = os.getcwd()

# Append the correct paths
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_dir, 'appLib'))

# Import statements
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is correctly defined in SlotMapper.py
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your GUI code here...
