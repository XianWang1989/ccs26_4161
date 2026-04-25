
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib'))

try:
    from SlotMapper import SlotMap
    print("SlotMap imported successfully!")
except ImportError as e:
    print("ImportError:", e)
