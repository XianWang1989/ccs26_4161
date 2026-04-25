
import os
import sys

# Append directories to PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Try importing after modifying sys.path
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Ensure SlotMap is defined
if 'SlotMap' in dir():
    print("SlotMap imported successfully.")

# Proceed with the rest of the imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
