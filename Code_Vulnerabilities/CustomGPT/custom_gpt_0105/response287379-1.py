
import os
import sys

current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_dir, 'appLib'))

from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined here
