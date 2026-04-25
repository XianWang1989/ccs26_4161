
import os
import sys

# Append the necessary directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging - Print sys.path to verify correct paths
print("Current sys.path:", sys.path)

# Try importing after verifying paths
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
