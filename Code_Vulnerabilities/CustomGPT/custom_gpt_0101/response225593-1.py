
import tkinter as tk
from tkinter.filedialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')

mGui = tk.Tk()
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
