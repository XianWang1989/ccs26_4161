
import Tkinter as tk
from Tkinter import Button
from Tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))

# Create the main window
mGui = tk.Tk()
mGui.title('File Browser')

# Create a button to browse files
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the application
mGui.mainloop()
