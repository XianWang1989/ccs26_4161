
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open file dialog and store the filename
    filename = askopenfilename()
    if filename:
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))
        print("File saved:", filename)

# Create the main GUI window
mGui = tk.Tk()
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
