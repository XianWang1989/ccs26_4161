
from Tkinter import Tk, Button, filedialog

def browse_file():
    # Open the file dialog and get the filename
    filename = filedialog.askopenfilename()
    if filename:
        # Write the filename to a text file
        with open("output.txt", "w") as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f'File saved: {filename}')

# Set up the main application window
mGui = Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
