
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    # Ask the user to select a file
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open the file to write
            conf.write(f'receptor="{filename}"\n')  # Write the filename

# Create the main window
mGui = Tk()

# Create a Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the main event loop
mGui.mainloop()
