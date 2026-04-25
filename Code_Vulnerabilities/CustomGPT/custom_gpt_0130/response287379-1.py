
import os
import sys

# Ensure you are appending the correct path.
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Verify paths for debugging
print("Current sys.path:", sys.path)

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import failed: {e}")

# Import other necessary components
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Additional code for your GUI setup can follow...
