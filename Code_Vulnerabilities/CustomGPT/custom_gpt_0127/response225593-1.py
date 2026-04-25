
import Tkinter as tk  # Use 'import tkinter' for Python 3
from tkFileDialog import askopenfilename  # Use 'from tkinter import filedialog' for Python 3

def browse_file():
    filename = askopenfilename()  # Open the file dialog and store the selected file name
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file for writing
            conf.write(f'receptor="{filename}"\n')  # Write the file name

# Create the main window
mGui = tk.Tk()
mGui.title("Select File")
mGui.geometry("600x200")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
