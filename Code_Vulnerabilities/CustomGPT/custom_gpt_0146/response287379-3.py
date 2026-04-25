
import os
import sys

# Update the path to include the appLib folder
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Print sys.path to debug
print(sys.path)

from SlotMapper import SlotMap
# Rest of your imports
