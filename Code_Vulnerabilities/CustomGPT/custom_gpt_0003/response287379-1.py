
import os
import sys

# Assuming your project structure is:
# .
# ├── appLib
# │   ├── __init__.py
# │   ├── KB-GUI
# │   │   ├── __init__.py
# │   │   ├── your_gui_file.py
# │   ├── SlotMapper.py      <-- This file must exist here
# │   ├── ShelfTypeSelection.py
# │   └── PackTypeSelection.py
#
# Make sure the path to appLib is correctly appended
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import statements must follow the structure of the directories
from tkinter import *
# Ensure SlotMapper is being imported from the correct modified path
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector

# Proceed with your GUI code
