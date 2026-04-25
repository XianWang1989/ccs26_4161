
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the selected filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open the text file in append mode
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to the text file

mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)  # Update command to call browse_file
browsebutton.place(x=400, y=50)

mGui.mainloop()
