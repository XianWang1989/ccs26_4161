
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open (or create) a text file
            conf.write("receptor='{0}'\n".format(filename))  # Write the filename to the file
        print("File saved:", filename)  # Print confirmation to console

# Set up the Tkinter GUI
mGui = tk.Tk()
mGui.title('File Browser')

browsebutton = Button(mGui, text='Browse', command=browse_file)  # Link button to function
browsebutton.place(x=400, y=50)  # Position the button

mGui.mainloop()  # Run the GUI
