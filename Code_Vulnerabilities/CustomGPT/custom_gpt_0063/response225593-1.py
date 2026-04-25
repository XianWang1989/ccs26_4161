
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file for writing
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to the text file
        print("File selected:", filename)  # Print the selected file name

# Set up the GUI
mGui = tk.Tk()
mGui.title("File Browser")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)  # Use the browse_file function
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
