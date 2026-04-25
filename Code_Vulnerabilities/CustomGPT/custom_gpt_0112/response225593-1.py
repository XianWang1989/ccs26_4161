
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Ensure a file was selected
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f'Selected file: {filename}')  # Optional: print to console

# Setup the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Set the window size
mGui.geometry("500x150")

# Start the GUI event loop
mGui.mainloop()
