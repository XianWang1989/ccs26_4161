
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open file dialog and get the file name
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        # Write the file name to conf.txt
        with open('conf.txt', 'a') as conf:
            conf.write(f"receptor='{filename}'\n")
        print(f'Selected file: {filename}')  # Optional: Print to console

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
