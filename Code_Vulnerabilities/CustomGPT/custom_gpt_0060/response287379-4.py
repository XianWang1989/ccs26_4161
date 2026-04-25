
import os
import sys

# Correctly set the path to include the appLib directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'appLib'))

from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector

# Now you can use SlotMap and other imports as needed
