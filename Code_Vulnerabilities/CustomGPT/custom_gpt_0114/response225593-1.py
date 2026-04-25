
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file to write
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file

# Create the main GUI window
mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
