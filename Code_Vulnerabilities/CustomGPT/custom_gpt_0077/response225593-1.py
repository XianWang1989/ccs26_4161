
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the selected file name
    filename = askopenfilename()
    if filename:
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved:", filename)

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the application
mGui.mainloop()
