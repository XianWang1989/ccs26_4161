
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the selected file path
    file_path = askopenfilename()

    if file_path:
        # Write the file path to a text file
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(file_path))

        print("File saved:", file_path)

# Set up the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter main loop
mGui.mainloop()
