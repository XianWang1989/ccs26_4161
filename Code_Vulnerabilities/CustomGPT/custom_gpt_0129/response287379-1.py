
import os
import sys

# Add the directory containing appLib to the Python path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Optional: Print the sys.path for debugging
print("Current Python path:", sys.path)

# Attempt to import SlotMap after ensuring the path is set
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Other imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your main code would go here...
