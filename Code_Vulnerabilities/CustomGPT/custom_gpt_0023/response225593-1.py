
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog
    if filename:  # Ensure a file was selected
        with open("output.txt", "a") as conf:  # Append file
            conf.write(f'receptor="{filename}"\n')
        print(f'Selected file: {filename}')  # Print to console

# Create main window
mGui = tk.Tk()
mGui.title("File Selector")
mGui.geometry("600x200")

# Create Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the Tkinter event loop
mGui.mainloop()
