
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved:", filename)

mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)
mGui.mainloop()
