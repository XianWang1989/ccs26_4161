
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # make sure a file is selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))

# Set up the GUI
mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
