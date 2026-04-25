
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the filename
    if filename:  # Ensure a file was selected
        with open('output.txt', 'a') as conf:  # Open the file in append mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Create the main GUI window
mGui = Tk()
mGui.title("File Selector")

# Create a browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the main loop
mGui.mainloop()
