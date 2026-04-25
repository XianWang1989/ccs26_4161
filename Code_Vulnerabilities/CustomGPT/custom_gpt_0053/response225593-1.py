
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the filename
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        print("Selected file:", filename)  # Optional: print the filename to console
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:  # Change 'output.txt' as needed
            conf.write('receptor="{}"\n'.format(filename))

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
