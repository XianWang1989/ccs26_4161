
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Get the filename from askopenfilename
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open the text file for writing
            conf.write("receptor='" + filename + "'\n")
        print("File saved:", filename)  # Optional: print the filename to console

# Create the main window
mGui = tk.Tk()
mGui.geometry("600x200")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the application
mGui.mainloop()
