
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))

# Create the main GUI window
mGui = tk.Tk()

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
