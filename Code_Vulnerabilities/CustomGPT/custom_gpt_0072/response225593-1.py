
from Tkinter import Tk, Button, filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))

mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
