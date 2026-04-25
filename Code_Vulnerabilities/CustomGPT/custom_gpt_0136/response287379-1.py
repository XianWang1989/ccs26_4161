
import os
import sys

# Print current working directory
print("Current working directory:", os.getcwd())

# Append the target directories to sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)
print("Updated Python Path:", sys.path)

# Attempt to import the modules
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print("ImportError:", e)
