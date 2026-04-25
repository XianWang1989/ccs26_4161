
import os
import sys

# Add the appLib directory to the PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Now you can import your modules
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap
slot_map_instance = SlotMap()
