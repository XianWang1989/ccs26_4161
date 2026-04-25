
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the dialog to select a file
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file in write mode
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename

# Create the main GUI window
mGui = Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
