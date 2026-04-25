
import os
import sys

# Modify PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Import modules (ensure SlotMapper is accessible)
try:
    from SlotMapper import SlotMap  # Adjust if needed
except ImportError as e:
    print(f"ImportError: {e}")

from tkinter import *

# Example usage of SlotMap (ensure this is valid)
if 'SlotMap' in locals():
    # Assuming SlotMap is a class or function
    slot_map_instance = SlotMap()  # Example of using SlotMap
else:
    print("SlotMap could not be imported.")
