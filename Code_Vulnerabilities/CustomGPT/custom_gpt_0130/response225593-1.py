
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Ensure a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved:", filename)

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI loop
mGui.mainloop()
