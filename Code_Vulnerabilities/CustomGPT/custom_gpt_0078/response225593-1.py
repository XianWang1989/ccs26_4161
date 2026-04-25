
import tkinter as tk
from tkinter import Button, filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write(f"receptor='{filename}'\n")
        print(f"File saved: {filename}")  # Optional: print the filename

# Setting up the GUI
mGui = tk.Tk()
mGui.title("File Browser")

browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
