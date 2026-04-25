
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open your text file
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Create the main window
mGui = tk.Tk()
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)  # Use the new function
browsebutton.place(x=400, y=50)

mGui.mainloop()
