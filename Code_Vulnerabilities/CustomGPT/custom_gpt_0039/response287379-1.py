
import os
import sys

# Print current working directory for debugging
print("Current working directory:", os.getcwd())

# Append directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debug: Check updated sys.path
print("Updated sys.path:", sys.path)

try:
    from tkinter import *
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print("ImportError:", e)
