
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open (or create) a text file to write to
            conf.write('receptor="{}"\n'.format(filename))  # Write the selected file name to the text file

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")
mGui.geometry("500x200")

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=50)

# Start the GUI event loop
mGui.mainloop()
