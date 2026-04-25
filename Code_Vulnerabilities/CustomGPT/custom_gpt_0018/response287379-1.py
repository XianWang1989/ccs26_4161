
import os
import sys

# Add the appLib directory to sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Import SlotMapper directly from appLib
from appLib.SlotMapper import SlotMap
from appLib.ShelfTypeSelection import ShelfTypeSelector
from appLib.PackTypeSelection import PackTypeSlotMappingSelector
from appLib.EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your code...
