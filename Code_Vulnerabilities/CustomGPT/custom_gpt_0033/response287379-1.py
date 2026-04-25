
import os
import sys

# Ensure the correct path is appended
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Importing necessary modules
from tkinter import *
from SlotMapper import SlotMap  # Ensure SlotMap is defined in SlotMapper.py

# Check if SlotMap can be accessed
try:
    print(SlotMap)  # Check if SlotMap is accessible
except ImportError as e:
    print(f"ImportError: {e}")

# Continue with your GUI setup
class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My Application")

    def run(self):
        # Your application logic here
        pass

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
