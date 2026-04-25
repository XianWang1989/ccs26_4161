
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the file name
    if filename:  # Ensure a file was selected
        with open('output.txt', 'w') as conf:  # Open (or create) a text file
            conf.write(f"receptor='{filename}'\n")  # Write the filename to the file
        print(f"File selected: {filename}")  # Optional: print the filename to the console

# Create the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI
mGui.mainloop()
