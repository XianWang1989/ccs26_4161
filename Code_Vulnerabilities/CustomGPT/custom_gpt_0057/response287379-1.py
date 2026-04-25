
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print("Current sys.path:", sys.path)

try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")
    print("Check if the module path is correct and that SlotMap exists in SlotMapper.py.")

# Example usage of SlotMap (ensure SlotMap is defined in SlotMapper)
if 'SlotMap' in locals():
    print("SlotMap imported successfully.")
else:
    print("SlotMap could not be imported. Verify the module structure.")
