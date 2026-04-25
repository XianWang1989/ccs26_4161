
# Directory structure:
# project/
# ├── appLib/
# │   ├── __init__.py
# │   └── SlotMapper.py
# └── main.py

# SlotMapper.py
class SlotMap:
    def __init__(self):
        print("SlotMap initialized.")

# main.py
import os
import sys

# Adjusting sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print("Python Path:", sys.path)

try:
    from SlotMapper import SlotMap
    slot_map = SlotMap()
except ImportError as e:
    print("ImportError:", e)
