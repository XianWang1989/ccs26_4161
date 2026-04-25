
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write('receptor="{0}"\n'.format(filename))
        print("File saved:", filename)

# Set up Tkinter GUI
mGui = Tk()
mGui.title("File Browser")

browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
