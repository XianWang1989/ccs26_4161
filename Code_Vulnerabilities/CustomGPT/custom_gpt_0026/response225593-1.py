
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open the output file
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the file

# Create the main window
mGui = tk.Tk()
mGui.title('File Browser')

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
