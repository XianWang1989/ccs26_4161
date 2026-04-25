
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the selected file name
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open the output file in write mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file
        print("File written to output.txt")  # Optional: Print confirmation

# Create the main GUI window
mGui = tk.Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
