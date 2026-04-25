
import os
import sys

# Modifying the Python path to include the directories
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Debugging output to check sys.path
print("Current Python Path:", sys.path)

from tkinter import *
from SlotMapper import SlotMap         # Ensure SlotMapper.py is in the correct path

# Your GUI code here
def main():
    root = Tk()
    slot_map = SlotMap()  # Creating an instance of SlotMap
    root.mainloop()

if __name__ == '__main__':
    main()
