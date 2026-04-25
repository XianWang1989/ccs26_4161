
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open file dialog
    if filename:
        with open("output.txt", "w") as conf:  # Write to a text file
            conf.write("receptor='{}'\n".format(filename))

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
