
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Open the file dialog and get the filename
    filename = filedialog.askopenfilename()

    # If a file was selected, write to the configuration file
    if filename:
        with open('config.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f'Selected file: {filename} written to config.txt')

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
