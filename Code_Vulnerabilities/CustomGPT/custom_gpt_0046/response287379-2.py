
import os
import sys

# Ensure the path to appLib is correctly added
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage
if __name__ == "__main__":
    slot_map = SlotMap()
    # Additional code here
