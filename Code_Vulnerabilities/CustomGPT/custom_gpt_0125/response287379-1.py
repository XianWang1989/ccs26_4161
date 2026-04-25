
import os
import sys

# Add the directories to the Python path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Ensure that all imports are done after modifying sys.path
from tkinter import *
from SlotMapper import SlotMap  # This should now work if SlotMapper is correctly placed
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap
if __name__ == "__main__":
    # Your application logic here
    pass
