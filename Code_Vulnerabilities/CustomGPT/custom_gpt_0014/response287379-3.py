
import os
import sys

# Add the appLib directory to the sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Debugging: Print the sys.path
print("Current sys.path:", sys.path)

# Try importing SlotMap
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)

# Other imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
