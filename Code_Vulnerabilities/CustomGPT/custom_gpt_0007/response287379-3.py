
import os
import sys

# Dynamically adding to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
from SlotMapper import SlotMap  # Ensure SlotMapper.py is in appLib

# Now you can use SlotMap
slot_map_instance = SlotMap()
