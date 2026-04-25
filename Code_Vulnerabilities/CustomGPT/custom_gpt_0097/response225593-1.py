
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file is selected
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')
        print("File saved:", filename)

# Set up the GUI
mGui = tk.Tk()
mGui.title('File Selector')

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
