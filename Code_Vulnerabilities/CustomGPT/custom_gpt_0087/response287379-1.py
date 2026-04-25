
import os
import sys

# Assuming the structure is as follows:
# current_directory/
# ├── appLib/
# │   ├── __init__.py
# │   ├── KB-GUI/
# │   │   ├── __init__.py
# │   │   ├── SlotMapper.py
# │   │   ├── ShelfTypeSelection.py
# │   │   ├── PackTypeSelection.py
# │   │   └── EntryWidgets.py
# └── main_script.py

sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Importing after adjusting sys.path
from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Further code...
