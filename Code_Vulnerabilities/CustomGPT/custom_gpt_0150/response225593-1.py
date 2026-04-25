
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open text file for writing
            conf.write(f'receptor="{filename}"\n')  # Write filename to file
        print(f'Selected file: {filename}')  # Print to console for confirmation

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")
mGui.geometry("600x200")

# Create a 'Browse' button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
