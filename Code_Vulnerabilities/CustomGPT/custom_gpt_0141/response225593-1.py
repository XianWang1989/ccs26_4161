
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open a file dialog and get the selected file path
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open the output file in append mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file
        print("Selected file:", filename)  # Optional: Print the filename to console

# Create the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
