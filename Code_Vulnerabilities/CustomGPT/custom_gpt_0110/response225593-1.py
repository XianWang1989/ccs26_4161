
import Tkinter as tk
from tkinter.filedialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Ensure a file was selected
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to a text file
        print("File saved:", filename)  # Optionally print the filename

# Set up the main application window
mGui = tk.Tk()
mGui.title("File Selector")

# Create a Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter event loop
mGui.mainloop()
