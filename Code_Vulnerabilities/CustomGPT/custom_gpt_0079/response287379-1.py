
import os
import sys

# Adjust the path to include the appLib directory
sys.path.append(os.path.join(os.getcwd(), 'appLib'))
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Import necessary libraries and your modules
from tkinter import Tk, Label
from SlotMapper import SlotMap   # Ensure SlotMap is defined in SlotMapper.pyw
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage
def main():
    root = Tk()
    label = Label(root, text="Hello, World!")
    label.pack()

    # Instantiate SlotMap (make sure SlotMap is a class or function)
    slot_map = SlotMap()
    root.mainloop()

if __name__ == "__main__":
    main()
