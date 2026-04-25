
import os
import sys

# Add the necessary directories to the system path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Check if SlotMap can be imported
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Error importing SlotMap: {e}")
    print("Available items in SlotMapper:", dir(SlotMapper))  # Debugging line

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Rest of your code...
