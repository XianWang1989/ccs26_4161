
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a text file to write
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Create the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter event loop
mGui.mainloop()
