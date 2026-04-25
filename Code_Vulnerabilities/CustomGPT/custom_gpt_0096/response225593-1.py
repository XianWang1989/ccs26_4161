
import tkinter as tk
from tkinter import Button
from tkinter.filedialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Make sure a file was selected
        with open('output.txt', 'a') as conf:
            conf.write("receptor='{}'\n".format(filename))

# Setting up the main GUI
mGui = tk.Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
