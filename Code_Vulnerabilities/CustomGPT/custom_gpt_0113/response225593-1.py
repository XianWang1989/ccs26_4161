
from tkinter import Tk, Button, filedialog

def browse_file():
    # Open file dialog and get the file path
    filename = filedialog.askopenfilename()
    if filename:
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')

# Set up the main GUI
mGui = Tk()
mGui.title("File Selector")

# Create and place the Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
