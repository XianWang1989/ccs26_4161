
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Append to the output file
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename
        print('Selected file:', filename)  # Optional: Print to console

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the application
mGui.mainloop()
