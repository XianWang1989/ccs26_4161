
import os
import sys
from pathlib import Path

# Get the current working directory
current_dir = Path(os.getcwd())
app_lib_dir = current_dir / 'appLib' / 'KB-GUI'

# Add the appLib directory and its parent to the Python path
if app_lib_dir.exists() and app_lib_dir.is_dir():
    sys.path.append(str(app_lib_dir))
sys.path.append(str(current_dir / 'appLib'))

# Print the sys.path for debugging
print("Current sys.path:")
print(sys.path)

# Attempting the import after modifying sys.path
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")
