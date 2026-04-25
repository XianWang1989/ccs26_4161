
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    file_name = askopenfilename()  # Open file dialog
    if file_name:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open output file
            conf.write('receptor="{}"\n'.format(file_name))  # Write file name

# Initialize Tkinter
mGui = tk.Tk()
mGui.geometry('500x200')

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
