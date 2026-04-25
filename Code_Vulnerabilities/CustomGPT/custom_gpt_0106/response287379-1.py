
import os
import sys

# Update sys.path to include appLib directory
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Import necessary modules
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code here
if __name__ == "__main__":
    # Initialize your application
    pass
