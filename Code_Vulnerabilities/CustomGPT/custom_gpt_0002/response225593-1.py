
from Tkinter import *
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))

mGui = Tk()
mGui.geometry('600x150')

browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
