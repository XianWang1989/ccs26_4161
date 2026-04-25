
from Tkinter import *
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the selected filename
    if filename:  # Ensure that a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file for writing
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the file
        print("File saved as:", filename)

# Create the main window
mGui = Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
