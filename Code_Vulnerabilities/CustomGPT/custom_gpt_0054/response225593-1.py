
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open a file dialog and get the selected file's path
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a file to write the path
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file
        print("File path written to output.txt: {}".format(filename))  # Optional: print to console

# Create the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter event loop
mGui.mainloop()
