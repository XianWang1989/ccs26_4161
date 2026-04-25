
import os
import sys

# Adjust the sys.path to include the right directories
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Print sys.path to debug
print(sys.path)

# Import your modules
try:
    from SlotMapper import SlotMap
    print("SlotMap imported successfully!")
except ImportError as e:
    print("ImportError:", e)

# Continue with other imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
