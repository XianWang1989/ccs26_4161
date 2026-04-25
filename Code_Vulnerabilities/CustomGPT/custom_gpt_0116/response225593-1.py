
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog to select a file
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open file to append
            conf.write(f'receptor="{filename}"\n')  # Write the filename

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
