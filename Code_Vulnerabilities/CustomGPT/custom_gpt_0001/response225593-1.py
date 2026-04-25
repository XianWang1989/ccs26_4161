
from Tkinter import Tk, Button, filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open file dialog and get the filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file to write
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file

# Set up the main application window
mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)  # Command is the browse_file function
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Run the GUI loop
