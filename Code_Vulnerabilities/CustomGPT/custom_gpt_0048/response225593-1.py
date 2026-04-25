
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open file for writing
            conf.write("receptor='{}'\n".format(filename))  # Write filename to file
        print("File selected:", filename)  # Optional: print the selected file name

# Set up the GUI
mGui = tk.Tk()
mGui.title("File Browser")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
