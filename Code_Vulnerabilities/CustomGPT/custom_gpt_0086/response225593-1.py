
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open dialog to select file
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open text file for writing
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Create the main application window
mGui = tk.Tk()
mGui.title("File Selector")

# Create a button that triggers the browse_file function
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
