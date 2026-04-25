
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print("Python Path:", sys.path)

try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)
