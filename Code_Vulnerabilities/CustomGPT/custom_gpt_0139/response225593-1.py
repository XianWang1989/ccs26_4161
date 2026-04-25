
import Tkinter as tk  # Use `import tkinter as tk` for Python 3
from tkFileDialog import askopenfilename  # Use `from tkinter import filedialog` for Python 3

def browse_file():
    # Open file dialog and get the selected file name
    filename = askopenfilename()
    if filename:  # Ensure a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print(f"File saved as: {filename}")

# Create a Tkinter window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI loop
mGui.mainloop()
