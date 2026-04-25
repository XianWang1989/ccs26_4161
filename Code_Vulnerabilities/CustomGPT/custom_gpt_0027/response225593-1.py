
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open the file in append mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI event loop
mGui.mainloop()
