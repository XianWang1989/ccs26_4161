
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open the output file
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the file
        print(f'Selected file: {filename}')  # Optional: print the filename to console

# Set up the main Tkinter window
mGui = Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter main loop
mGui.mainloop()
