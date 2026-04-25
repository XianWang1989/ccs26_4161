
import os
import sys

# Add the parent directory of appLib to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Now import your modules
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
