
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_and_write():
    # Open file dialog to select a file
    filename = askopenfilename()

    # Check if filename is not empty
    if filename:
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File name written to output.txt:", filename)

# Create main Tkinter window
mGui = tk.Tk()
mGui.title("File Selector")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_and_write)
browsebutton.place(x=400, y=50)

# Run the Tkinter event loop
mGui.mainloop()
