
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open file dialog and store the selected file path
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open file to write
            conf.write('receptor="{}"\n'.format(filename))  # Write path to file
        print("File saved:", filename)

# Create GUI
mGui = tk.Tk()
mGui.title("File Browser")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
