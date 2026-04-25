
import os
import sys

# Add the appLib directory to Python path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

from SlotMapper import SlotMap
