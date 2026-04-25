
import os
import sys

# Assuming your project structure is like this:
# /project
# ├── appLib
# │   ├── KB-GUI
# │   │   ├── GUI_file.py
# │   │   └── SlotMapper.py
# │   └── other_modules.py

# Make sure to set the correct paths
current_working_dir = os.getcwd()
sys.path.append(os.path.join(current_working_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_working_dir, 'appLib'))

# Import your modules
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMapper.py contains the SlotMap definition
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
