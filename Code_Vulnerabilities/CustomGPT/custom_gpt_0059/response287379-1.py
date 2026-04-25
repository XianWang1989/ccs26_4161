
import os
import sys

# Ensure correct path to your modules
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Print the sys.path for debugging
print(sys.path)

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Import other necessary modules
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Continue with your code...
