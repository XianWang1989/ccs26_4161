
import os
import sys

# Modify PYTHONPATH first
current_directory = os.getcwd()
sys.path.append(os.path.join(current_directory, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_directory, 'appLib'))

# Check if the paths are correctly set
print("Current sys.path:")
print(sys.path)

# Import statements - ensure these are in the correct order and logic
try:
    from SlotMapper import SlotMap  # Importing this first
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# You can add additional tests here to ensure imports work
