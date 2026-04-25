
import tkinter as tk
from tkinter import filedialog

def browse_file():
    # Open the file dialog and get the selected file name
    filename = filedialog.askopenfilename()
    if filename:  # If a file is selected
        # Open a text file in write mode
        with open('output.txt', 'w') as conf:
            # Write the selected filename to the text file
            conf.write(f"receptor='{filename}'\n")
        print("File path saved to output.txt")

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser Example")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI main loop
mGui.mainloop()
