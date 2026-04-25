
import os
import sys

# Ensure correct directory is added to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Now attempt to import
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")

# Example usage
if __name__ == "__main__":
    # Your application logic here
    pass
