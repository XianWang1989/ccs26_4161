
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the dialog and get the selected file
    if filename:  # Check if a file was selected
        # Print the filename to a text file
        with open('output.txt', 'a') as conf:  # Open in append mode
            conf.write("receptor='{}'\n".format(filename))
        print("Selected file:", filename)  # Optional: print to console for feedback

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
