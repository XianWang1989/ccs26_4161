
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a file to write
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the file
        print(f'File selected: {filename}')  # Print to console (optional)

mGui = tk.Tk()
mGui.title("File Browser")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
