
import tkinter as tk
from tkinter import Button
from tkFileDialog import askopenfilename  # For Python 2.5

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a text file to write
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button
browse_button = Button(mGui, text='Browse', command=browse_file)
browse_button.place(x=400, y=50)

# Run the GUI event loop
mGui.mainloop()
