
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write("receptor='{}'\n".format(filename))

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
