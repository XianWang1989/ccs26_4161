
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the selected file path
    file_path = askopenfilename()
    if file_path:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(file_path))

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the main loop
mGui.mainloop()
