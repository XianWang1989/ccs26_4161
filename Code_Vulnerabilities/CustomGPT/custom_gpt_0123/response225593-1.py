
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Open file dialog and store the selected filename
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved:", filename)

# Create the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the application
mGui.mainloop()
