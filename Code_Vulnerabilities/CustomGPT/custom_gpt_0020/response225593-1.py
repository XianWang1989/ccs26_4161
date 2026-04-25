
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the filename
    file_path = askopenfilename()

    if file_path:  # Check if a file was selected
        # Write the selected filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(file_path))
        print("Filename written to output.txt")  # Optional confirmation

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
