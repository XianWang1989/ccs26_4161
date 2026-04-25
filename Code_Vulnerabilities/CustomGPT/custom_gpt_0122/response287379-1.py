
import os
import sys

# Add the directory containing your modules to sys.path
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_dir, 'appLib'))

# Check if SlotMapper can be imported
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Remaining imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
