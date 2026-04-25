
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to the text file

# Create the main application window
mGui = tk.Tk()
mGui.title("File Selector")

# Create a 'Browse' button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
