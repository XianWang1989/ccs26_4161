
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='" + filename + "'\n")
        print("File selected:", filename)  # Optional: print to console

# Create the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter main loop
mGui.mainloop()
