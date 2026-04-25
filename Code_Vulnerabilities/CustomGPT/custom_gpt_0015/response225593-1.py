
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the file path
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open text file to write
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")
mGui.geometry("600x200")

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=250, y=50)

# Start the GUI event loop
mGui.mainloop()
