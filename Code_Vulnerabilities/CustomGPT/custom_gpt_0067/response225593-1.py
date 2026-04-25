
import Tkinter as tk
from Tkinter import filedialog

def browse_callback():
    filename = filedialog.askopenfilename()
    if filename:
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))

# Create the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_callback)
browsebutton.place(x=400, y=50)

# Run the application
mGui.mainloop()
