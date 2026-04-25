
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open (or create) a text file
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
