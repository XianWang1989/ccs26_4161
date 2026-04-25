
import os
import sys

# Dynamically add the application library paths
app_lib_path = os.path.join(os.getcwd(), 'appLib')
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')
sys.path.append(app_lib_path)
sys.path.append(kb_gui_path)

# Check the modified sys.path
print("Current PYTHONPATH:", sys.path)

# Now attempt to import
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")

# Rest of your GUI code...
