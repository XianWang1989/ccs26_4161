
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open file in append mode
            conf.write("receptor='{}'\n".format(filename))

# Create a simple GUI
mGui = tk.Tk()
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
