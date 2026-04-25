
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Ask the user for a file and store the filename
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to a text file

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI loop
mGui.mainloop()
