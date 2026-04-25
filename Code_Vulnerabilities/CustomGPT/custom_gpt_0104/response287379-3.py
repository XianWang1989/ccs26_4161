
import os
import sys

# Ensure you're appending the correct path to your 'appLib' directory
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Optional: Print the current sys.path to debug
print("Current sys.path:")
for path in sys.path:
    print(path)

from tkinter import *
# Assuming your SlotMapper.py contains a defined SlotMap class
from SlotMapper import SlotMap  
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Now you can use SlotMap
slot_map = SlotMap()
