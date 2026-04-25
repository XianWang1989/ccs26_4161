
from Tkinter import *
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a filename was selected
        with open("output.txt", "a") as conf:  # Open the file in append mode
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to the text file

# Create the main window
mGui = Tk()
mGui.title("Browse File Example")
mGui.geometry("500x200")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=50)

mGui.mainloop()
