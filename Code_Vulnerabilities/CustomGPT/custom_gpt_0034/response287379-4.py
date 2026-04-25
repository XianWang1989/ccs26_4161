
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

from tkinter import *
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example class using SlotMap
class MyApp:
    def __init__(self, master):
        self.slot_map = SlotMap()
        # Initialize your GUI components here

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
