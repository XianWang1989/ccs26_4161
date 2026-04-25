
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging: Check the contents of appLib
print("Current Working Directory:", os.getcwd())
print("PYTHONPATH:", sys.path)
print("Files in appLib:")
print(os.listdir(os.path.join(os.getcwd(), 'appLib')))

from SlotMapper import SlotMap
