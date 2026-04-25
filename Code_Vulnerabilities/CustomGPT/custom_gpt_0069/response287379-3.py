
import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print(sys.path)  # Check if the directories are included

from SlotMapper import SlotMap  # Attempt to import here
