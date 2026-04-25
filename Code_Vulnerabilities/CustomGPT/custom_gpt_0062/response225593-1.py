
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get file path
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open the text file in write mode
            conf.write('receptor="{}"\n'.format(filename))  # Write the file path to the text file

# Set up the GUI
mGui = tk.Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
