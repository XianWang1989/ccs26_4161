
import os
import sys

# Adjust the path
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

try:
    from SlotMapper import SlotMap
    print("Import successful!")
except ImportError as e:
    print("ImportError:", e)
