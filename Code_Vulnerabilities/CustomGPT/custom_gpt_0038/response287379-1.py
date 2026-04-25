
import os
import sys

# Ensure this points to your correct directory
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Check if SlotMapper is accessible
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from tkinter import *

# Your GUI code here, for example:
root = Tk()

# You can utilize SlotMap now, if imported successfully
# slot_map_instance = SlotMap()  # use `SlotMap` class here

root.mainloop()
