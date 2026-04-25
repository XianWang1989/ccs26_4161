
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print(sys.path)  # Check if the correct paths are added

from SlotMapper import SlotMap  # Ensure this line is placed after sys.path is updated
