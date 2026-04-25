
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open output file
            conf.write("receptor='{}'\n".format(filename))  # Write filename to file

# Set up the main GUI
mGui = tk.Tk()
mGui.title("File Selector")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
