
import os
import sys

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Append paths
app_lib_path = os.path.join(os.getcwd(), 'appLib')
gui_path = os.path.join(app_lib_path, 'KB-GUI')

sys.path.append(gui_path)
sys.path.append(app_lib_path)

# Print sys.path for debugging
print("System Path:", sys.path)

# Attempt to import
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
