
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_and_save():
    # Open file dialog to select a file
    filename = askopenfilename()
    if filename:  # Ensure a file was selected
        # Open a text file to write the filename
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))

# Create the main window
mGui = Tk()
mGui.title("File Selector")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_and_save)
browsebutton.place(x=400, y=50)

# Run the GUI
mGui.mainloop()
