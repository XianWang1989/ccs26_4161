
import os
import sys

# Append directories to sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
gui_path = os.path.join(app_lib_path, 'KB-GUI')

sys.path.append(gui_path)
sys.path.append(app_lib_path)

# Debugging: Print sys.path to confirm the paths
print("Current sys.path:")
for p in sys.path:
    print(p)

# Import your modules
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")

from tkinter import *
