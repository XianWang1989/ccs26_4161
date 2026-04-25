
import os
import sys

# Get the current working directory
current_dir = os.getcwd()

# Add the appLib directory and any needed subdirectories to Python's path
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_dir, 'appLib'))

# Import required libraries
from tkinter import *

# Import your modules after modifying sys.path
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")
