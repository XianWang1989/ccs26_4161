
import os
import sys

# Print the current working directory
print(f"Current Working Directory: {os.getcwd()}")

# Add paths to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Verify the paths added
print("Current sys.path:")
for p in sys.path:
    print(p)

from tkinter import *
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

# Continue with your GUI code

class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My Application")

        # Example usage of SlotMap
        self.slot_map = SlotMap()  # Ensure SlotMap is correctly imported

        # Add your GUI elements here

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
