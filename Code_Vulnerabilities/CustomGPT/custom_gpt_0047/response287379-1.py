
import os
import sys

# Add the appLib directory to the system path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

from KB_GUI.SlotMapper import SlotMap  # Adjust the import statement
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
