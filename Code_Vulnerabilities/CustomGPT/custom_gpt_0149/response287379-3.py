
# Directory structure
appLib/
├── __init__.py
├── SlotMapper.py
└── KB-GUI/
    ├── __init__.py
    └── GUI_module.py

# SlotMapper.py
class SlotMap:
    def __init__(self):
        print("SlotMap Created")

# GUI_module.py
import os
import sys

# Adjusting sys.path
sys.path.insert(0, os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.insert(0, os.path.join(os.getcwd(), 'appLib'))

from SlotMapper import SlotMap

# Use SlotMap in your GUI module
slot_map_instance = SlotMap()
