
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the selected file name
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved:", filename)  # Print the filename to the console

# Create the main Tkinter window
mGui = Tk()
mGui.title("File Browse Example")

# Create and place the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter main loop
mGui.mainloop()
