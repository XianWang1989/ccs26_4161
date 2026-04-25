
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open text file to write
            conf.write(f'receptor="{filename}"\n')  # Write the filename

# Set up the main GUI window
mGui = tk.Tk()
mGui.geometry("600x400")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Run the GUI event loop
