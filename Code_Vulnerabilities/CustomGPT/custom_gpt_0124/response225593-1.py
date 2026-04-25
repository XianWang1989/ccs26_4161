
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open text file for writing
            conf.write("receptor='{}'\n".format(filename))  # Write filename to file

# Create main window
mGui = tk.Tk()
mGui.title("File Browser")
mGui.geometry("500x200")

# Create browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=50)

# Start the GUI loop
mGui.mainloop()
