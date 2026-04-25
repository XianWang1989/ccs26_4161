
import os
import sys

# Add application libraries to the system path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Print sys.path for debugging
print("Current sys.path:", sys.path)

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your GUI code...
