
import tkinter as tk
from tkinter import Button, filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open("output.txt", "w") as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f'Selected file: {filename}')

# Create the main GUI window
mGui = tk.Tk()
mGui.geometry("600x200")

# Create a Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the main loop
mGui.mainloop()
