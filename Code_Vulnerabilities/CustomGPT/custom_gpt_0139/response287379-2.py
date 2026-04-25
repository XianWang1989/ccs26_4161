
import os
import sys
import tkinter as tk

# Append application library paths
app_lib_path = os.path.join(os.getcwd(), 'appLib')
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')

# Add paths to sys.path
sys.path.append(kb_gui_path)
sys.path.append(app_lib_path)

# Print the sys.path for debugging purposes
print("Current sys.path:", sys.path)

# Now perform the imports after the paths have been added
from SlotMapper import SlotMap
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your Tkinter application code starts here
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("300x200")

        # Example usage of SlotMap, ShelfTypeSelector, etc.
        self.slot_map = SlotMap()
        # Add components and logic as needed

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
