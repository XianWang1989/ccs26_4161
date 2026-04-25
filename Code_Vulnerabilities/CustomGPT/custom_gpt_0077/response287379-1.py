
import os
import sys

# Define the path to the application library
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Check if SlotMapper.py exists in the directory
if 'SlotMapper.py' in os.listdir(app_lib_path):
    print("SlotMapper.py found in appLib.")
else:
    print("SlotMapper.py not found!")

# Now attempt the import
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Import other modules
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
